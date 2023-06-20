## Batch

Batch step type (e.g. Batch(1) defines 1 batch)

---

## Epoch

Epoch step type (e.g. Epoch(1) defines 1 epoch)

---

## PyTorchTrial

PyTorch trials are created by subclassing this abstract class.

We can do the following things in this trial class:

* **Define models, optimizers, and LR schedulers**.

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

### (self) -> Dict[str, determined.pytorch._callback.PyTorchCallback]

Defines a dictionary of string names to callbacks to be used during
training and/or validation.

The string name will be used as the key to save and restore callback
state for any callback that defines :meth:`load_state_dict` and :meth:`state_dict`.

### (self) -> determined.pytorch._data.DataLoader

Defines the data loader to use during training.

Must return an instance of :py:class:`determined.pytorch.DataLoader`.

### (self) -> determined.pytorch._data.DataLoader

Defines the data loader to use during validation.

Must return an instance of :py:class:`determined.pytorch.DataLoader`.

### (self, batch: Union[Dict[str, torch.Tensor], Sequence[torch.Tensor], torch.Tensor], batch_idx: int) -> Dict[str, Any]

Calculate validation metrics for a batch and return them as a
dictionary mapping metric names to metric values. Per-batch validation metrics
are reduced (aggregated) to produce a single set of validation metrics for the
entire validation set (see :meth:`evaluation_reducer`).

There are two ways to specify evaluation metrics. Either override
:meth:`evaluate_batch` or :meth:`evaluate_full_dataset`. While
:meth:`evaluate_full_dataset` is more flexible,
:meth:`evaluate_batch` should be preferred, since it can be
parallelized in distributed environments, whereas
:meth:`evaluate_full_dataset` cannot. Only one of
:meth:`evaluate_full_dataset` and :meth:`evaluate_batch` should be
overridden by a trial.

The metrics returned from this function must be JSON-serializable.

Arguments:
    batch (Dict[str, torch.Tensor], Sequence[torch.Tensor], torch.Tensor):
        batch of data for evaluating.
    batch_idx (integer): index of the current batch among all the epochs processed
        per device (slot) since the start of training.

### (self, data_loader: torch.utils.data.dataloader.DataLoader) -> Dict[str, Any]

Calculate validation metrics on the entire validation dataset and
return them as a dictionary mapping metric names to reduced metric
values (i.e., each returned metric is the average or sum of that metric
across the entire validation set).

This validation cannot be distributed and is performed on a single
device, even when multiple devices (slots) are used for training. Only
one of :meth:`evaluate_full_dataset` and :meth:`evaluate_batch` should
be overridden by a trial.

The metrics returned from this function must be JSON-serializable.

Arguments:
    data_loader (torch.utils.data.DataLoader): data loader for evaluating.

### (self) -> Union[determined.pytorch._reducer.Reducer, Dict[str, determined.pytorch._reducer.Reducer]]

Return a reducer for all evaluation metrics, or a dict mapping metric
names to individual reducers. Defaults to :obj:`determined.pytorch.Reducer.AVG`.

### (self, batch: Any) -> int

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

### (self, batch: Union[Dict[str, torch.Tensor], Sequence[torch.Tensor], torch.Tensor], epoch_idx: int, batch_idx: int) -> Union[torch.Tensor, Dict[str, Any]]

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

---

## ShouldExit

ShouldExit breaks out of the top-level train loop from inside function calls.

---

## TrainUnit

TrainUnit is the base class for the supported training units (Batch, Epoch) containing
the value of unit, where the value can be an int or an implementable collections.abc.Container.

TrainUnits are used to define periodic training behavior such as checkpointing and validating.

int values are treated as periods, e.g. Batch(100) will checkpoint/validate every 100 batches.
collections.abc.Container values are treated as schedules, e.g. Batch(1,5,10) will
checkpoint/validate on batches 1, 5, and 10.

---

## _TrainBoundaryType

An enumeration.

---

