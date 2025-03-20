# Scripts for OpenWebUI Public Model Index

This directory contains scripts used to maintain and update the OpenWebUI Public Model Index repository.

## Scripts Overview

### csv_to_json.py
Converts the source CSV file to a JSON format for easier programmatic access.
- **Input**: `../source-data/models.csv`
- **Output**: `../converted/models.json`

### csv_to_markdown.py
Generates individual markdown files for each model in the CSV file.
- **Input**: `../source-data/models.csv`
- **Output**: Individual files in `../individual-configs/` directory
- Tracks changes using a memory file to avoid unnecessary rewrites

### generate_index.py
Creates an alphabetical index of all models in the README.md file.
- **Input**: `../source-data/models.csv`
- **Output**: Updates the `../README.md` file with an alphabetical listing of all models
- Uses HTML comment markers to identify where to insert the index

## Batch Script

For convenience, a batch script is provided in the root directory:

### update_repository.sh
Runs all three scripts in sequence to fully update the repository after changes to the CSV file.

## Usage

To update the entire repository after modifying the CSV file:

```bash
# From the repository root
./update_repository.sh
```

To run individual scripts:

```bash
# From the repository root
python3 scripts/csv_to_json.py
python3 scripts/csv_to_markdown.py
python3 scripts/generate_index.py
```
