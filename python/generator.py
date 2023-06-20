#!/usr/bin/env python

import inspect
import sys
import os
import importlib.util

# Specify the Python file to document
PYTHON_FILE = "test.py"

# Specify the output Markdown file
OUTPUT_FILE = "documentation.md"

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

    # Process each class in the module
    for name, cls in inspect.getmembers(module, inspect.isclass):
        # Get the class docstring
        class_docstring = inspect.getdoc(cls)

        # Skip classes without docstrings
        if not class_docstring:
            continue

        # Print the class heading
        print(f"## {name}\n")
        print(f"{class_docstring}\n")

        # Process each method in the class
        for method_name, method in inspect.getmembers(cls, inspect.isfunction):
            # Skip special and private methods
            if method_name.startswith("__"):
                continue

            # Get the method signature
            method_signature = inspect.signature(method)

            # Get the method docstring
            method_docstring = inspect.getdoc(method)

            # Skip methods without docstrings
            if not method_docstring:
                continue

            # Print the method heading
            print(f"### {method_signature}\n")
            print(f"{method_docstring}\n")

        # Add a separator after each class
        print("---\n")

    # Reset the standard output
    sys.stdout = sys.__stdout__
