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

