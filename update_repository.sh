#!/bin/bash
# update_repository.sh
# Script to update the repository by running all the necessary scripts

# Set the base directory to the script's location
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$BASE_DIR"

echo "===== OpenWebUI Public Model Index Repository Update ====="
echo "Starting repository update process..."

# Create necessary directories if they don't exist
mkdir -p individual-configs
mkdir -p converted
mkdir -p memory

# Step 1: Convert CSV to JSON
echo -e "\n[1/3] Converting CSV to JSON..."
python3 scripts/csv_to_json.py
if [ $? -eq 0 ]; then
    echo "✓ CSV to JSON conversion completed successfully"
else
    echo "✗ CSV to JSON conversion failed"
    exit 1
fi

# Step 2: Generate individual markdown files
echo -e "\n[2/3] Generating individual markdown files..."
python3 scripts/csv_to_markdown.py
if [ $? -eq 0 ]; then
    echo "✓ Individual markdown files generated successfully"
else
    echo "✗ Failed to generate individual markdown files"
    exit 1
fi

# Step 3: Update the README.md with the alphabetical index
echo -e "\n[3/3] Updating README.md with alphabetical index..."
python3 scripts/generate_index.py
if [ $? -eq 0 ]; then
    echo "✓ README.md updated successfully with alphabetical index"
else
    echo "✗ Failed to update README.md"
    exit 1
fi

echo -e "\n===== Repository Update Completed Successfully ====="
echo "The following files were updated:"
echo "- converted/models.json"
echo "- individual-configs/*.md (individual model files)"
echo "- README.md (with alphabetical index)"
echo ""
echo "You can now commit these changes to your repository."
