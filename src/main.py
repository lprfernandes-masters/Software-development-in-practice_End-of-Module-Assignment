import json
import os
from datetime import datetime

FILE_NAME = 'records.json'


class RecordManager:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = file_name
        self.records = []  # Internal storage as a list of dictionaries.
        self.load_records()

    def load_records(self):
        """Load records from the file if it exists."""
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r') as f:
                    self.records = json.load(f)
                print(f"Loaded {len(self.records)} records.")
            except Exception as e:
                print(f"Error loading records: {e}")
                self.records = []
        else:
            self.records = []

    def save_records(self):
        """Save the current records to the file."""
        try:
            with open(self.file_name, 'w') as f:
                json.dump(self.records, f, indent=4)
            print("Records saved successfully.")
        except Exception as e:
            print(f"Error saving records: {e}")

    def generate_id(self, record_type: str):
        """Generate a new unique ID for a given record type ('Client' or 'Airline')."""
        ids = [rec["ID"] for rec in self.records
               if rec.get("Type") == record_type and rec.get("ID") is not None]
        return max(ids, default=0) + 1

    def is_unique_id(self, record_type: str, id_value: int, ignore_index: int = None):
        """Check if the provided id_value is unique among records of record_type.
           If ignore_index is provided, that record is skipped (useful during updates)."""
        for idx, rec in enumerate(self.records):
            if rec.get("Type") == record_type:
                if ignore_index is not None and idx == ignore_index:
                    continue
                if rec.get("ID") == id_value:
                    return False
        return True
