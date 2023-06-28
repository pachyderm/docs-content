#!/usr/bin/env python

import inspect
import sys
import os
import importlib.util
import re

# Specify the Python files to document
PYTHON_FILES = ["pytorch.py", "context.py"]

# Specify the output Markdown file
OUTPUT_FILE = "api-reference.md"

# Initialize a dictionary to store the classes and their headings
class_headings = {}

# Process each Python file
for python_file in PYTHON_FILES:
    # Get the absolute path to the Python file
    python_file_path = os.path.abspath(python_file)

    # Get the module name from the file path
    module_name = os.path.splitext(os.path.basename(python_file_path))[0]

    # Load the Python module
    spec = importlib.util.spec_from_file_location(module_name, python_file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    # Process each class in the module
    for name, cls in inspect.getmembers(module, inspect.isclass):
        # Get the class docstring
        class_docstring = inspect.getdoc(cls)

        # Skip classes without docstrings
        if not class_docstring:
            continue

        # Store the class heading in the dictionary
        class_headings[name] = f"## {name}"

# Open the output file for writing
with open(OUTPUT_FILE, "w") as f:
    # Redirect the standard output to the file
    sys.stdout = f

    # Generate YAML front matter (title, description, etc.)
    print("---")
    print("title: API Reference")
    print("description: API Reference for PyTorch and Context")
    print("tags: [python]")
    print("---")

    # Process each Python file again
    for python_file in PYTHON_FILES:
        # Get the absolute path to the Python file
        python_file_path = os.path.abspath(python_file)

        # Get the module name from the file path
        module_name = os.path.splitext(os.path.basename(python_file_path))[0]

        # Load the Python module
        spec = importlib.util.spec_from_file_location(module_name, python_file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        # Process each class in the module
        for name, cls in inspect.getmembers(module, inspect.isclass):
            # Get the class docstring
            class_docstring = inspect.getdoc(cls)

            # Skip classes without docstrings
            if not class_docstring:
                continue

            # Replace :class: mentions with hyperlinks to the class headings
            class_docstring = re.sub(
                r":class:`~?([\w\.]+)`",
                lambda match: f"[{match.group(1)}](#{match.group(1).replace('.', '-')})" if match.group(1).replace('.', '-') in class_headings else match.group(0),
                class_docstring,
            )

            # Print the modified class docstring
            print(f"{class_headings.get(name)}\n")
            print(f"{class_docstring}\n")

    # Reset the standard output
    sys.stdout = sys.__stdout__
