import os
import re

# Define the regular expression pattern for identifying the "SEE ALSO" header
see_also_pattern = re.compile(r'###\s*SEE\s+ALSO', re.IGNORECASE)

def process_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find the index of the "SEE ALSO" header using the regular expression pattern
    match = see_also_pattern.search(content)
    if match:
        # Extract content before the "SEE ALSO" header
        modified_content = content[:match.start()]
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)
        
        print(f"Processed: {file_path}")
    else:
        print(f"No 'SEE ALSO' header found in: {file_path}")

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                process_markdown_file(file_path)

if __name__ == "__main__":
    target_directory = "."  # Change this to the directory where your markdown files are located
    process_directory(target_directory)
