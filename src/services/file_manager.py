import json
import os


def load_records(file_name='src/data/records.json'):
    """Load records from a JSON file if it exists."""
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            try:
                records = json.load(f)
                print(f"Loaded {len(records)} records.")
                return records
            except Exception as e:
                print(f"Error loading records: {e}")
                return []
    return []


def save_records(records, file_name='src/data/records.json'):
    """Save the current records to a JSON file."""
    with open(file_name, 'w') as f:
        try:
            json.dump(records, f, indent=4)
        except Exception as e:
            print(f"Error saving records: {e}")
