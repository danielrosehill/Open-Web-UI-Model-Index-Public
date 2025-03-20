#!/usr/bin/env python3
"""
Script to generate an alphabetical index in markdown format from a CSV file
and update the README.md file with this index.
"""

import csv
import os
import re
from pathlib import Path
import argparse

def read_csv_data(csv_file_path):
    """Read the CSV file and return a list of dictionaries."""
    models = []
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            models.append(row)
    return models

def generate_index_markdown(models):
    """Generate the markdown index from the models data."""
    # Sort models alphabetically by name
    sorted_models = sorted(models, key=lambda x: x['name'].lower())
    
    markdown_lines = []
    
    for model in sorted_models:
        name = model['name']
        description = model['description']
        url = model['url']
        
        # Create the config file path
        config_file_name = name.lower().replace(' ', '-').replace('/', '-')
        config_file_path = f"individual-configs/{config_file_name}.md"
        
        # Generate the markdown for this model
        markdown_lines.append(f"## {name}\n")
        markdown_lines.append(f"{description}\n")
        markdown_lines.append(f"[View in Repo](individual-configs/{config_file_name}.md) | ")
        markdown_lines.append(f"[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)]({url})\n")
    
    return "\n".join(markdown_lines)

def update_readme(readme_path, index_markdown):
    """Update the README.md file with the generated index."""
    # Define start and end markers for the index section
    start_marker = "<!-- START_MODEL_INDEX -->"
    end_marker = "<!-- END_MODEL_INDEX -->"
    
    # Check if README exists, if not create a basic one
    if not os.path.exists(readme_path):
        with open(readme_path, 'w', encoding='utf-8') as file:
            file.write("# Openwebui-Public-Model-Index\n\n")
            file.write(f"{start_marker}\n{end_marker}\n")
        print(f"Created new README.md file at {readme_path}")
    
    # Read the current README content
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if markers exist, if not add them
    if start_marker not in content or end_marker not in content:
        if end_marker in content and start_marker not in content:
            content = content.replace(end_marker, f"{start_marker}\n{end_marker}")
        elif start_marker in content and end_marker not in content:
            content = content.replace(start_marker, f"{start_marker}\n{end_marker}")
        else:
            content += f"\n\n{start_marker}\n{end_marker}\n"
        print("Added index markers to README.md")
    
    # Replace the content between the markers with the new index
    pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    replacement = f"{start_marker}\n{index_markdown}\n{end_marker}"
    updated_content = pattern.sub(replacement, content)
    
    # Write the updated content back to the README
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"Updated README.md with the model index")

def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(description='Generate model index for README.md')
    parser.add_argument('--csv', default='../source-data/models.csv', 
                        help='Path to the CSV file (default: ../source-data/models.csv)')
    parser.add_argument('--readme', default='../README.md',
                        help='Path to the README.md file (default: ../README.md)')
    args = parser.parse_args()
    
    # Get the absolute paths
    base_dir = Path(__file__).parent.absolute()
    csv_path = base_dir / args.csv
    readme_path = base_dir / args.readme
    
    print(f"Reading CSV data from {csv_path}")
    models = read_csv_data(csv_path)
    print(f"Found {len(models)} models in the CSV file")
    
    print("Generating markdown index...")
    index_markdown = generate_index_markdown(models)
    
    print(f"Updating README at {readme_path}")
    update_readme(readme_path, index_markdown)
    
    print("Done!")

if __name__ == "__main__":
    main()
