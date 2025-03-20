import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    """Converts a CSV file to a JSON file.

    Args:
        csv_file_path (str): The path to the CSV file.
        json_file_path (str): The path to the output JSON file.
    """
    data = []
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(json_file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

# Example usage:
csv_file = 'source-data/models.csv'
json_file = 'converted/models.json'
csv_to_json(csv_file, json_file)