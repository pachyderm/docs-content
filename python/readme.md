# Docstrings to Markdown Test

The purpose of this test is to test that docstrings from python files can be processed and output as a markdown documentation page. The purpose is also to test that any mention of a class or method is a clickable link, is properly formatted, and when clicked, navigates to the section where the class or method is documented.

## Test Files

- generator.py is the script that processes the docstrings and creates an output markdown file
- pytorch.py is the first file to document
- context.py is the second file to document

## How it Works in Sphinx

There are several files in the determined harness/determined/pytorch directory that contain docstrings that make up the content of the Pytorch reference page at https://docs.determined.ai/latest/reference/training/api-pytorch-reference.html. This is accomplished through docstrings and sphinx autodocs.

For example, the "class PyTorchTrial(det.Trial):" starts on line 1379 of the python script, and documents methods and classes, e.g.,

    * **Define models, optimizers, and LR schedulers**.

      In the :meth:`__init__` method, initialize models, optimizers, and LR schedulers
      and wrap them with ``wrap_model``, ``wrap_optimizer``, ``wrap_lr_scheduler``
      provided by :class:`~determined.pytorch.PyTorchTrialContext`.

where :meth:`__init__` method is a reference to the @abstractmethod that starts on line 1413 and contains docstrings.

    @abstractmethod
        def __init__(self, context: pytorch.PyTorchTrialContext) -> None:

and :class:`~determined.pytorch.PyTorchTrialContext` is a reference to an entirely different python script, _pytorch_context.py starting at line 33:

    class PyTorchTrialContext(pytorch._PyTorchReducerContext):
    """Contains runtime information for any Determined workflow that uses the ``PyTorch`` API.

At build time, CircleCI builds the docs via the sphinx.ext.autodoc extension that then takes these docstrings and prints them in the rst page, api-pytorch-reference.rst. It does this via the sphinx autoclass directives.

The technical writer manually adds the relevant sphinx autoclass directive to the .rst page. For example:

    .. autoclass:: determined.pytorch.PyTorchTrial...  

Furthermore, Sphinx formats each autoclass directive according to its role, e.g., :class: or :meth:, and makes each instance a clickable link. The link takes the user to the heading to find out more about the class or method or function. For example, instead of literally printing ":class:`~determined.pytorch.PyTorchTrialContext`", the sphinx autodoc extension prints 

    provided by PyTorchTrialContext.

What is happening behind the link PyTorchTrialContext is the autodoc extension is going out into the harness/determined/pytorch/ directory and finding class PyTorchTrialContext within the file _pytorch_context.py.

