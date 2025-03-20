#!/usr/bin/env python3
import csv
import json
import os
import re
import hashlib
from pathlib import Path

# Define paths
SOURCE_CSV = 'source-data/models.csv'
MEMORY_FILE = 'memory/last_run_state.json'
OUTPUT_DIR = 'individual-configs'

def sanitize_filename(name):
    """Convert a model name to a sanitized filename.
    
    Args:
        name (str): The model name to sanitize.
        
    Returns:
        str: A sanitized filename (lowercase, spaces to hyphens, no special chars).
    """
    # Convert to lowercase and replace spaces with hyphens
    sanitized = name.lower().replace(' ', '-')
    # Remove any characters that aren't alphanumeric, hyphens, or underscores
    sanitized = re.sub(r'[^a-z0-9\-_]', '', sanitized)
    return sanitized

def generate_markdown(model):
    """Generate markdown content for a model.
    
    Args:
        model (dict): The model data.
        
    Returns:
        str: Markdown content for the model.
    """
    # Create the badge link - use the full URL to ensure correct linking
    badge_url = f"[![Use on OpenWebUI](https://img.shields.io/badge/Use%20on-OpenWebUI-blue)]({model['url']})"
    
    # Format the system prompt with proper markdown code block
    system_prompt = model['system_prompt'].replace('\n', '\n')
    
    # Generate the markdown content
    markdown = f"""# {model['name']}

{badge_url}

## Description

{model['description']}

## System Prompt

```
{system_prompt}
```

## Link

{model['url']}
"""
    return markdown

def calculate_hash(model):
    """Calculate a hash for a model to detect changes.
    
    Args:
        model (dict): The model data.
        
    Returns:
        str: A hash representing the model's content.
    """
    # Create a string representation of the model and hash it
    model_str = json.dumps(model, sort_keys=True)
    return hashlib.md5(model_str.encode()).hexdigest()

def load_memory():
    """Load the memory of the last run state.
    
    Returns:
        dict: A dictionary mapping filenames to model hashes.
    """
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_memory(memory):
    """Save the memory of the current run state.
    
    Args:
        memory (dict): A dictionary mapping filenames to model hashes.
    """
    # Ensure the memory directory exists
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

def main():
    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Load the memory from the last run
    memory = load_memory()
    
    # Track current models for deletion detection
    current_models = set()
    
    # Read the CSV file
    with open(SOURCE_CSV, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Sanitize the model name for the filename
            filename = sanitize_filename(row['name'])
            filepath = os.path.join(OUTPUT_DIR, f"{filename}.md")
            
            # Calculate the hash of the current model
            model_hash = calculate_hash(row)
            
            # Add to current models set
            current_models.add(filename)
            
            # Check if the file exists and if the content has changed
            if filename in memory and memory[filename] == model_hash:
                # Model hasn't changed, skip
                continue
            
            # Generate the markdown content
            markdown = generate_markdown(row)
            
            # Write the markdown to a file
            with open(filepath, 'w') as f:
                f.write(markdown)
            
            # Update the memory
            memory[filename] = model_hash
    
    # Remove files for models that no longer exist
    for filename in list(memory.keys()):
        if filename not in current_models:
            filepath = os.path.join(OUTPUT_DIR, f"{filename}.md")
            if os.path.exists(filepath):
                os.remove(filepath)
            # Remove from memory
            del memory[filename]
    
    # Save the updated memory
    save_memory(memory)
    
    print(f"Successfully processed {len(current_models)} models.")

if __name__ == "__main__":
    main()