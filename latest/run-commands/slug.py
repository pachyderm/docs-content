import os
import re

directory_path = "./"  # Replace with the actual path to your directory

# Define a regular expression pattern to match the slug attribute
pattern = r"slug:\s*\"[^\"]*\"\n"

def process_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    
    new_content = re.sub(pattern, "", content)
    
    with open(file_path, "w") as file:
        file.write(new_content)

if os.path.isdir(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".md"):
            file_path = os.path.join(directory_path, filename)
            process_file(file_path)
            print(f"Processed: {file_path}")
else:
    print("Invalid directory path.")
