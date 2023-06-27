#!/usr/bin/env python

import inspect
import sys
import os
import importlib.util
import re

# Specify the Python file to document
PYTHON_FILE = "pytorch.py"

# Specify the output Markdown file
OUTPUT_FILE = "api-pytorch-reference.md"

# Get the absolute path to the Python file
python_file_path = os.path.abspath(PYTHON_FILE)

# Get the module name from the file path
module_name = os.path.splitext(os.path.basename(python_file_path))[0]

# Load the Python module
spec = importlib.util.spec_from_file_location(module_name, python_file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

# Open the output file for writing
with open(OUTPUT_FILE, "w") as f:
    # Redirect the standard output to the file
    sys.stdout = f

    # Generate yaml front matter (title, description, etc.) using the class name
    
    title = f"title: {module.__name__} module"
    description = f"description: {module.__spec__.name} module"

    print("---")
    print(title)
    print(description)
    print("tags: [python]")
    print("---")


    # Process each class in the module
    for name, cls in inspect.getmembers(module, inspect.isclass):

        # Get the class docstring
        class_docstring = inspect.getdoc(cls)

        # Skip classes without docstrings
        if not class_docstring:
            continue

        # Convert :class: mentions into bookmark links
        # Example: :class:`~determined.pytorch.PyTorchTrial`
        # get the module name by removing everything but the text between the two periods.
        class_docstring = re.sub(
            r":class:`~?determined\.([^`]+)`",
            lambda match: "[:{}](#{}-module-{})".format(
                match.group(1),
                match.group(1).split(".")[-2].lower().replace(".", "-"),
                match.group(1).split(".")[-1].lower().replace(".", "-")
            ),
            class_docstring,
        )

        
        # Print the class heading
        print(f"## {name}\n")
        print(f"{class_docstring}\n")

        # Process each method in the class
        for method_name, method in inspect.getmembers(cls, inspect.isfunction):
            # Skip special and private methods
            if method_name.startswith("__"):
                # rename __init__ to constructor
                if method_name == "__init__":
                    method_name = name + "Constructor"

            # Get the method signature
            method_signature = inspect.signature(method)

            # Get the method docstring
            method_docstring = inspect.getdoc(method)

            # Skip methods without docstrings
            if not method_docstring:
                continue

            # Convert :meth: mentions into bookmark links
            method_docstring = re.sub(
                r":meth:`([^`]+)`",
                lambda match: "[:{}](#{})".format(match.group(1), module_name.lower() + "-module-" + match.group(1).lower()),
                method_docstring,
            )

            
            # Print the method heading
            print(f"### {method_name}\n")
            print(f"`{method_signature}`\n")
            print(f"{method_docstring}\n")

        # Add a separator after each class
        print("---\n")

    # Reset the standard output
    sys.stdout = sys.__stdout__
