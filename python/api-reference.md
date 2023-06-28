---
title: API Reference
description: API Reference for PyTorch and Context
tags: [python]
---
## PyTorchTrial

PyTorch trials are created by subclassing this abstract class.

We can do the following things in this trial class:

* **Define models, optimizers, and LR schedulers**.

  TEST THAT THE METHOD LINKS TO THE ABSTRACT METHOD SECTION
  TEST THAT THE CLASS LINKS TO THE PYTORCHTRIALCONTEXT SECTION
  WHICH IS ACTUALLY SOURCED FROM ANOTHER SCRIPT CONTEXT DOT PY
  
  In the :meth:`__init__` method, initialize models, optimizers, and LR schedulers
  and wrap them with ``wrap_model``, ``wrap_optimizer``, ``wrap_lr_scheduler``
  provided by :class:`~determined.pytorch.PyTorchTrialContext`.

* **Run forward and backward passes**.

  In :meth:`train_batch`, call ``backward`` and ``step_optimizer`` provided by
  :class:`~determined.pytorch.PyTorchTrialContext`.
  We support arbitrary numbers of models, optimizers, and LR schedulers
  and arbitrary orders of running forward and backward passes.

* **Configure automatic mixed precision**.

  In the :meth:`__init__` method, call ``configure_apex_amp`` provided by
  :class:`~determined.pytorch.PyTorchTrialContext`.

* **Clip gradients**.

  In :meth:`train_batch`, pass a function into
  ``step_optimizer(optimizer, clip_grads=...)`` provided by
  :class:`~determined.pytorch.PyTorchTrialContext`.

### build_callbacks

`(self) -> Dict[str, determined.pytorch._callback.PyTorchCallback]`

Defines a dictionary of string names to callbacks to be used during
training and/or validation.

The string name will be used as the key to save and restore callback
state for any callback that defines [:load_state_dict](#pytorch-module-load_state_dict) and [:state_dict](#pytorch-module-state_dict).

### build_training_data_loader

`(self) -> determined.pytorch._data.DataLoader`

Defines the data loader to use during training.

Must return an instance of :py:class:`determined.pytorch.DataLoader`.

### build_validation_data_loader

`(self) -> determined.pytorch._data.DataLoader`

Defines the data loader to use during validation.

Must return an instance of :py:class:`determined.pytorch.DataLoader`.

### evaluate_batch

`(self, batch: Union[Dict[str, torch.Tensor], Sequence[torch.Tensor], torch.Tensor], batch_idx: int) -> Dict[str, Any]`

Calculate validation metrics for a batch and return them as a
dictionary mapping metric names to metric values. Per-batch validation metrics
are reduced (aggregated) to produce a single set of validation metrics for the
entire validation set (see [:evaluation_reducer](#pytorch-module-evaluation_reducer)).

There are two ways to specify evaluation metrics. Either override
[:evaluate_batch](#pytorch-module-evaluate_batch) or [:evaluate_full_dataset](#pytorch-module-evaluate_full_dataset). While
[:evaluate_full_dataset](#pytorch-module-evaluate_full_dataset) is more flexible,
[:evaluate_batch](#pytorch-module-evaluate_batch) should be preferred, since it can be
parallelized in distributed environments, whereas
[:evaluate_full_dataset](#pytorch-module-evaluate_full_dataset) cannot. Only one of
[:evaluate_full_dataset](#pytorch-module-evaluate_full_dataset) and [:evaluate_batch](#pytorch-module-evaluate_batch) should be
overridden by a trial.

The metrics returned from this function must be JSON-serializable.

Arguments:
    batch (Dict[str, torch.Tensor], Sequence[torch.Tensor], torch.Tensor):
        batch of data for evaluating.
    batch_idx (integer): index of the current batch among all the epochs processed
        per device (slot) since the start of training.

### evaluate_full_dataset

`(self, data_loader: torch.utils.data.dataloader.DataLoader) -> Dict[str, Any]`

Calculate validation metrics on the entire validation dataset and
return them as a dictionary mapping metric names to reduced metric
values (i.e., each returned metric is the average or sum of that metric
across the entire validation set).

This validation cannot be distributed and is performed on a single
device, even when multiple devices (slots) are used for training. Only
one of [:evaluate_full_dataset](#pytorch-module-evaluate_full_dataset) and [:evaluate_batch](#pytorch-module-evaluate_batch) should
be overridden by a trial.

The metrics returned from this function must be JSON-serializable.

Arguments:
    data_loader (torch.utils.data.DataLoader): data loader for evaluating.

### evaluation_reducer

`(self) -> Union[determined.pytorch._reducer.Reducer, Dict[str, determined.pytorch._reducer.Reducer]]`

Return a reducer for all evaluation metrics, or a dict mapping metric
names to individual reducers. Defaults to :obj:`determined.pytorch.Reducer.AVG`.

### get_batch_length

`(self, batch: Any) -> int`

Count the number of records in a given batch.

Override this method when you are using custom batch types, as produced
when iterating over the :py:class:`determined.pytorch.DataLoader`.
For example, when using ``pytorch_geometric``:

.. code-block:: python

    # Extra imports:
    from determined.pytorch import DataLoader
    from torch_geometric.data.dataloader import Collater

    # Trial methods:
    def build_training_data_loader(self):
        return DataLoader(
            self.train_subset,
            batch_size=self.context.get_per_slot_batch_size(),
            collate_fn=Collater([], []),
        )

    def get_batch_length(self, batch):
        # `batch` is `torch_geometric.data.batch.Batch`.
        return batch.num_graphs

Arguments:
    batch (Any): input training or validation data batch object.

### train_batch

`(self, batch: Union[Dict[str, torch.Tensor], Sequence[torch.Tensor], torch.Tensor], epoch_idx: int, batch_idx: int) -> Union[torch.Tensor, Dict[str, Any]]`

Train on one batch.

Users should implement this function by doing the following things:

1. Run forward passes on the models.

2. Calculate the gradients with the losses with ``context.backward``.

3. Call an optimization step for the optimizers with ``context.step_optimizer``.
   You can clip gradients by specifying the argument ``clip_grads``.

4. Step LR schedulers if using manual step mode.

5. Return training metrics in a dictionary.

Here is a code example.

.. code-block:: python

    # Assume two models, two optimizers, and two LR schedulers were initialized
    # in ``__init__``.

    # Calculate the losses using the models.
    loss1 = self.model1(batch)
    loss2 = self.model2(batch)

    # Run backward passes on losses and step optimizers. These can happen
    # in arbitrary orders.
    self.context.backward(loss1)
    self.context.backward(loss2)
    self.context.step_optimizer(
        self.opt1,
        clip_grads=lambda params: torch.nn.utils.clip_grad_norm_(params, 0.0001),
    )
    self.context.step_optimizer(self.opt2)

    # Step the learning rate.
    self.lrs1.step()
    self.lrs2.step()

    return {"loss1": loss1, "loss2": loss2}

Arguments:
    batch (Dict[str, torch.Tensor], Sequence[torch.Tensor], torch.Tensor):
        batch of data for training.
    epoch_idx (integer): index of the current epoch among all the batches processed
        per device (slot) since the start of training.
    batch_idx (integer): index of the current batch among all the epochs processed
        per device (slot) since the start of training.
Returns:
    torch.Tensor or Dict[str, Any]:
        training metrics to return.

## ShouldExit

Common base class for all non-exit exceptions.

## _TrainBoundaryType

An enumeration.

## PyTorchTrialContext

Contains runtime information for any Determined workflow that uses the ``PyTorch`` API.

With this class, users can do the following things:

1. Wrap PyTorch models, optimizers, and LR schedulers with their Determined-compatible
   counterparts using :meth:`wrap_model`, :meth:`wrap_optimizer`, :meth:`wrap_lr_scheduler`,
   respectively. The Determined-compatible objects are capable of transparent
   distributed training, checkpointing and exporting, mixed-precision training,
   and gradient aggregation.
2. Configure apex amp by calling :meth:`configure_apex_amp` (optional).
3. Calculate the gradients with :meth:`backward` on a specified loss.
4. Run an optimization step with :meth:`step_optimizer`.
5. Functionalities inherited from :class:`determined.TrialContext`, including getting
   the runtime information and properly handling training data in distributed training.

### _filter_named_parameters

`(self, optimizer: torch.optim.optimizer.Optimizer) -> List`

_filter_named_parameters filters the named parameters of a specified optimizer out
of all the named parameters from a specified model. We need this function because
a ``torch.optim.Optimizer`` doesn't store parameter names, and we need the names of
the parameters when mapping parameters to each ``horovod.DistributedOptimizer``.

### backward

`(self, loss: torch.Tensor, gradient: Union[torch.Tensor, NoneType] = None, retain_graph: bool = False, create_graph: bool = False) -> None`

Compute the gradient of current tensor w.r.t. graph leaves.

The arguments are used in the same way as ``torch.Tensor.backward``.
See https://pytorch.org/docs/1.4.0/_modules/torch/tensor.html#Tensor.backward for details.

.. warning::
    When using distributed training, we don't support manual gradient accumulation.
    That means the gradient on each parameter can only be calculated once on each batch.
    If a parameter is associated with multiple losses, you can either choose to call
    ``backward'' on only one of those losses, or you can set the ``require_grads`` flag of
    a parameter or module to ``False`` to avoid manual gradient accumulation on that
    parameter.
    However, you can do gradient accumulation across batches by setting
    :ref:`optimizations.aggregation_frequency <config-aggregation-frequency>` in the
    experiment configuration to be greater than 1.

Arguments:
    gradient (Tensor or None): Gradient w.r.t. the
        tensor. If it is a tensor, it will be automatically converted
        to a Tensor that does not require grad unless ``create_graph`` is True.
        None values can be specified for scalar Tensors or ones that
        don't require grad. If a None value would be acceptable then
        this argument is optional.
    retain_graph (bool, optional): If ``False``, the graph used to compute
        the grads will be freed. Note that in nearly all cases setting
        this option to True is not needed and often can be worked around
        in a much more efficient way. Defaults to the value of
        ``create_graph``.
    create_graph (bool, optional): If ``True``, graph of the derivative will
        be constructed, allowing to compute higher order derivative
        products. Defaults to ``False``.

### configure_apex_amp

`(self, models: Union[torch.nn.modules.module.Module, List[torch.nn.modules.module.Module]], optimizers: Union[torch.optim.optimizer.Optimizer, List[torch.optim.optimizer.Optimizer]], enabled: Union[bool, NoneType] = True, opt_level: Union[str, NoneType] = 'O1', cast_model_type: Union[torch.dtype, NoneType] = None, patch_torch_functions: Union[bool, NoneType] = None, keep_batchnorm_fp32: Union[bool, str, NoneType] = None, master_weights: Union[bool, NoneType] = None, loss_scale: Union[str, float, NoneType] = None, cast_model_outputs: Union[torch.dtype, NoneType] = None, num_losses: Union[int, NoneType] = 1, verbosity: Union[int, NoneType] = 1, min_loss_scale: Union[float, NoneType] = None, max_loss_scale: Union[float, NoneType] = 16777216.0) -> Tuple`

Configure automatic mixed precision for your models and optimizers using NVIDIA's Apex
PyTorch extension. Note that details for ``apex.amp`` are handled automatically within
Determined after this call.

This function must be called **after** you have finished constructing your models and
optimizers with [:wrap_model](#context-module-wrap_model) and [:wrap_optimizer](#context-module-wrap_optimizer).

This function has the same arguments as
`apex.amp.initialize <https://nvidia.github.io/apex/amp.html#apex.amp.initialize>`_.

.. warning::
    When using distributed training and automatic mixed precision,
    we only support ``num_losses=1`` and calling backward on the loss once.

Arguments:
    models (``torch.nn.Module`` or list of ``torch.nn.Module`` s):  Model(s) to modify/cast.
    optimizers (``torch.optim.Optimizer`` or list of ``torch.optim.Optimizer`` s):
        Optimizers to modify/cast. REQUIRED for training.
    enabled (bool, optional, default=True):  If False, renders all Amp calls no-ops,
        so your script should run as if Amp were not present.
    opt_level (str, optional, default="O1"):  Pure or mixed precision optimization level.
        Accepted values are "O0", "O1", "O2", and "O3", explained in detail above.
    cast_model_type (``torch.dtype``, optional, default=None):  Optional property override,
        see above.
    patch_torch_functions (bool, optional, default=None):  Optional property override.
    keep_batchnorm_fp32 (bool or str, optional, default=None):  Optional property override.
        If passed as a string, must be the string "True" or "False".
    master_weights (bool, optional, default=None):  Optional property override.
    loss_scale (float or str, optional, default=None):  Optional property override.
        If passed as a string, must be a string representing a number, e.g., "128.0",
        or the string "dynamic".
    cast_model_outputs (torch.dtype, optional, default=None):  Option to ensure that
        the outputs of your model is always cast to a particular type regardless of
        ``opt_level``.
    num_losses (int, optional, default=1):  Option to tell Amp in advance how many
        losses/backward passes you plan to use.  When used in conjunction with the
        ``loss_id`` argument to ``amp.scale_loss``, enables Amp to use a different
        loss scale per loss/backward pass, which can improve stability.
        If ``num_losses`` is left to 1, Amp will still support multiple losses/backward
        passes, but use a single global loss scale for all of them.
    verbosity (int, default=1):  Set to 0 to suppress Amp-related output.
    min_loss_scale (float, default=None):  Sets a floor for the loss scale values that
        can be chosen by dynamic loss scaling.  The default value of None means that no
        floor is imposed. If dynamic loss scaling is not used, ``min_loss_scale`` is
        ignored.
    max_loss_scale (float, default=2.**24):  Sets a ceiling for the loss scale values
        that can be chosen by dynamic loss scaling.  If dynamic loss scaling is not used,
        ``max_loss_scale`` is ignored.

Returns:
    Model(s) and optimizer(s) modified according to the ``opt_level``.
    If  ``optimizers`` args were lists, the corresponding return value will
    also be a list.

### current_train_batch

`(self) -> int`

Current global batch index

### get_data_config

`(self) -> Dict[str, Any]`

Return the data configuration.

### get_experiment_id

`(self) -> int`

Return the experiment ID of the current trial.

### get_global_batch_size

`(self) -> int`

Return the global batch size.

### get_hparam

`(self, name: str) -> Any`

Return the current value of the hyperparameter with the given name.

### get_per_slot_batch_size

`(self) -> int`

Return the per-slot batch size. When a model is trained with a single GPU, this is equal to
the global batch size. When multi-GPU training is used, this is equal to the global batch
size divided by the number of GPUs used to train the model.

### get_stop_requested

`(self) -> bool`

Return whether a trial stoppage has been requested.

### get_tensorboard_path

`(self) -> pathlib.Path`

Get the path where files for consumption by TensorBoard should be written

### get_tensorboard_writer

`(self) -> Any`

This function returns an instance of ``torch.utils.tensorboard.SummaryWriter``

Trials users who wish to log to TensorBoard can use this writer object.
We provide and manage a writer in order to save and upload TensorBoard
files automatically on behalf of the user.

Usage example:

.. code-block:: python

   class MyModel(PyTorchTrial):
       def __init__(self, context):
           ...
           self.writer = context.get_tensorboard_writer()

       def train_batch(self, batch, epoch_idx, batch_idx):
           self.writer.add_scalar('my_metric', np.random.random(), batch_idx)
           self.writer.add_image('my_image', torch.ones((3,32,32)), batch_idx)

### get_trial_id

`(self) -> int`

Return the trial ID of the current trial.

### is_epoch_end

`(self) -> bool`

Returns true if the current batch is the last batch of the epoch.

.. warning::
    Not accurate for variable size epochs.

### is_epoch_start

`(self) -> bool`

Returns true if the current batch is the first batch of the epoch.

.. warning::
    Not accurate for variable size epochs.

### set_profiler

`(self, *args: List[str], **kwargs: Any) -> None`

``set_profiler()`` is a thin wrapper around the native PyTorch profiler, torch-tb-profiler.
It overrides the ``on_trace_ready`` parameter to the determined tensorboard path, while all
other arguments are passed directly into ``torch.profiler.profile``. Stepping the profiler
will be handled automatically during the training loop.

See the `PyTorch profiler plugin
<https://github.com/pytorch/kineto/tree/master/tb_plugin>`_ for details.

Examples:

Profiling GPU and CPU activities, skipping batch 1, warming up on batch 2, and profiling
batches 3 and 4.

.. code-block:: python

    self.context.set_profiler(
        activities=[
            torch.profiler.ProfilerActivity.CPU,
            torch.profiler.ProfilerActivity.CUDA,
        ],
        schedule=torch.profiler.schedule(
            wait=1,
            warmup=1,
            active=2
        ),
    )

### set_stop_requested

`(self, stop_requested: bool) -> None`

Set a flag to request a trial stoppage. When this flag is set to True,
we finish the step, checkpoint, then exit.

### step_optimizer

`(self, optimizer: torch.optim.optimizer.Optimizer, clip_grads: Union[Callable[[Iterator], NoneType], NoneType] = None, auto_zero_grads: bool = True, scaler: Union[Any, NoneType] = None) -> None`

Perform a single optimization step.

This function must be called once for each optimizer. However, the order of
different optimizers' steps can be specified by calling this function in different
orders. Also, gradient accumulation across iterations is performed by the Determined
training loop by setting the experiment configuration field
:ref:`optimizations.aggregation_frequency <config-aggregation-frequency>`.

Here is a code example:

.. code-block:: python

    def clip_grads(params):
        torch.nn.utils.clip_grad_norm_(params, 0.0001),

    self.context.step_optimizer(self.opt1, clip_grads)

Arguments:
    optimizer(``torch.optim.Optimizer``): Which optimizer should be stepped.
    clip_grads(a function, optional): This function should have one argument for
        parameters in order to clip the gradients.
    auto_zero_grads(bool, optional): Automatically zero out gradients automatically after
        stepping the optimizer. If false, you need to call ``optimizer.zero_grad()``
        manually. Note that if :ref:`optimizations.aggregation_frequency
        <config-aggregation-frequency>` is greater than 1, ``auto_zero_grads`` must be true.
    scaler(``torch.cuda.amp.GradScaler``, optional): The scaler to use for stepping the
        optimizer. This should be unset if not using AMP, and is necessary if
        ``wrap_scaler()`` was called directly.

### to_device

`(self, data: Union[Dict[str, Union[numpy.ndarray, torch.Tensor]], Sequence[Union[numpy.ndarray, torch.Tensor]], numpy.ndarray, torch.Tensor]) -> Union[Dict[str, torch.Tensor], Sequence[torch.Tensor], torch.Tensor]`

Map generated data to the device allocated by the Determined cluster.

All the data in the data loader and the models are automatically moved to the
allocated device. This method aims at providing a function for the data generated
on the fly.

### wrap_lr_scheduler

`(self, lr_scheduler: torch.optim.lr_scheduler._LRScheduler, step_mode: determined.pytorch._lr_scheduler.LRScheduler.StepMode, frequency: int = 1) -> torch.optim.lr_scheduler._LRScheduler`

Returns a wrapped LR scheduler.

The LR scheduler must use an optimizer wrapped by [:wrap_optimizer](#context-module-wrap_optimizer).  If ``apex.amp``
is in use, the optimizer must also have been configured with [:configure_apex_amp](#context-module-configure_apex_amp).

### wrap_model

`(self, model: torch.nn.modules.module.Module) -> torch.nn.modules.module.Module`

Returns a wrapped model.

### wrap_optimizer

`(self, optimizer: torch.optim.optimizer.Optimizer, backward_passes_per_step: int = 1, fp16_compression: Union[bool, NoneType] = None, average_aggregated_gradients: Union[bool, NoneType] = None) -> torch.optim.optimizer.Optimizer`

Returns a wrapped optimizer.

The optimizer must use the models wrapped by [:wrap_model](#context-module-wrap_model). This function
creates a ``horovod.DistributedOptimizer`` if using parallel/distributed training.

``backward_passes_per_step`` can be used to specify how many gradient aggregation
steps will be performed in a single ``train_batch`` call per optimizer step.
In most cases, this will just be the default value 1.  However, this advanced functionality
can be used to support training loops like the one shown below:

.. code-block:: python

    def train_batch(
        self, batch: TorchData, epoch_idx: int, batch_idx: int
    ) -> Dict[str, torch.Tensor]:
        data, labels = batch
        output = self.model(data)
        loss1 = output['loss1']
        loss2 = output['loss2']
        self.context.backward(loss1)
        self.context.backward(loss2)
        self.context.step_optimizer(self.optimizer, backward_passes_per_step=2)
        return {"loss1": loss1, "loss2": loss2}

### wrap_reducer

`(self, reducer: Union[Callable, determined.pytorch._reducer.MetricReducer], name: Union[str, NoneType] = None, for_training: bool = True, for_validation: bool = True) -> determined.pytorch._reducer.MetricReducer`

Register a custom reducer that will calculate a metric properly, even with distributed
training.

During distributed training and evaluation, many types of metrics must be calculated
globally, rather than calculating the metric on each shard of the dataset and averaged or
summed.  For example, an accurate ROC AUC for dataset cannot be derived from the individual
ROC AUC metrics calculated on by each worker.

Determined solves this problem by offering fully customizable metric reducers which are
distributed-aware.  These are registered by calling ``context.wrap_reducer()``
and are updated by the user during ``train_batch()`` or ``evaluate_batch()``.

Arguments:
    reducer (Union[Callable, pytorch.MetricReducer]):
        Either a reducer function or a pytorch.MetricReducer.  See below for more details.
    name: (Optional[str] = None):
        Either a string name to associate with the metric returned by the reducer, or
        ``None`` to indicate the metric will return a dict mapping string names to metric
        values.  This allows for a single reducer to return many metrics, such as for a
        per-class mean IOU calculation.  Note that if name is a string, the returned
        metric must NOT be a dict-type metric.
    for_training: (bool = True):
        Indicate that the ``reducer`` should be used for training workloads.
    for_validation: (bool = True):
        Indicate that the ``reducer`` should be used for validation workloads.

Return Value:
    pytorch.MetricReducer:
        If ``reducer`` was a function, the returned ``MetricReducer`` will have a single
        user-facing method like ``def update(value: Any) -> None`` that you should call
        during ``train_batch`` or ``evaluate_batch``.  Otherwise, the return value will
        just be the ``reducer`` that was passed in.

**Reducer functions: the simple API**

If the ``reducer`` parameter is a function, it must have the following properties:

   -  It accepts a single parameter, which will be a flat list of all inputs the users
      pass when they call ``.update()`` on the object returned by ``wrap_reducer()``.
      See the code example below for more details.
   -  It returns either a single (non-dict) metric or a dictionary mapping names to
      metrics, as described above.

The primary motivation for passing a function as the reducer is simplicity. Metrics from
all batches will be buffered in memory and passed over the network before they are reduced
all at once. This introduces some overhead, but it is likely unnoticeable for scalar
metrics or on validation datasets of small or medium size.  This single function strategy
can be useful for quick prototyping or for calculating metrics that are difficult
or impossible to calculate incrementally.

For example, ROC AUC could be properly calculated by passing a small wrapper function
calling ``sklearn.metrics.roc_auc_score``:

.. code-block:: python

   # Custom reducer function.
   def roc_auc_reducer(values):
       # values will be a flat list of all inputs to
       # .update(), which in this code example are
       # tuples of (y_true, y_score).  We reshape
       # that list into two separate lists:
       y_trues, y_scores = zip(*values)

       # Then we return a metric value:
       return sklearn.metrics.roc_auc_score(
           np.array(y_trues), np.array(y_scores)
       )

   class MyPyTorchTrial(PyTorchTrial):
       def __init__(self, context):
           self.roc_auc = context.wrap_reducer(
               roc_auc_reducer, name="roc_auc"
           )
           ...

       def evaluate_batch(self, batch):
           ...
           # Function-based reducers are updated with .update().
           # The roc_auc_reducer function will get a list of all
           # inputs that we pass in here:
           self.roc_auc.update((y_true, y_score))

           # The "roc_auc" metric will be included in the final
           # metrics after the workload has completed; no need
           # to return it here.  If that is your only metric,
           # just return an empty dict.
           return {}

**MetricReducer objects: the advanced API**

The primary motivation for passing a ``det.pytorch.MetricReducer`` as the reducer is
performance. ``det.pytorch.MetricReducer`` allows the user more control in how values are
stored and exposes a ``per_slot_reduce()`` call which lets users minimize the cost of the
network communication before the final ``cross_slot_reduce()``.

An additional reason for using the ``det.pytorch.MetricReducer`` is for flexibility of the
update mechanism, which is completely user-defined when subclassing ``MetricReducer``.

For the full details and a code example, see: :class:`~determined.pytorch.MetricReducer`.

### wrap_scaler

`(self, scaler: Any) -> Any`

Prepares to use automatic mixed precision through PyTorch’s native AMP API. The returned
scaler should be passed to ``step_optimizer``, but usage does not otherwise differ from
vanilla PyTorch APIs. Loss should be scaled before calling ``backward``, ``unscale_`` should
be called before clipping gradients, ``update`` should be called after stepping all
optimizers, etc.

PyTorch 1.6 or greater is required for this feature.

Arguments:
    scaler (``torch.cuda.amp.GradScaler``):  Scaler to wrap and track.

Returns:
    The scaler. It may be wrapped to add additional functionality for use in Determined.

