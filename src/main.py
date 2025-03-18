import json
import os
from datetime import datetime

FILE_NAME = 'records.json'

class RecordManager:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = file_name
        self.records = []  # Internal storage as a list of dictionaries.
        self.load_records()

    def add_record(self, record: dict):
        """Add a new record. For Client and Airline records, ensure a unique ID."""
        if record.get("Type") in ("Client", "Airline"):
            if record.get("ID") is None or not self.is_unique_id(record["Type"], record["ID"]):
                record["ID"] = self.generate_id(record["Type"])
        self.records.append(record)

    def delete_record(self, record: dict):
        """Delete the specified record."""
        try:
            self.records.remove(record)
            return True
        except ValueError:
            return False

    def update_record(self, index: int, new_record: dict):
        """Update a record at the given index. Ensure new IDs are unique for Client and Airline."""
        if self.records[index].get("Type") in ("Client", "Airline"):
            if new_record.get("ID") != self.records[index].get("ID"):
                if not self.is_unique_id(new_record["Type"], new_record.get("ID"), ignore_index=index):
                    print("Error: The provided ID is not unique. Update aborted.")
                    return False
        self.records[index] = new_record
        return True

    def search_records(self, record_type: str, search_key: str, search_value: str):
        """Generic search for Client or Airline records by matching key/value (case-insensitive)."""
        results = []
        for rec in self.records:
            if rec.get("Type") == record_type:
                if str(rec.get(search_key, "")).lower() == str(search_value).lower():
                    results.append(rec)
        return results

    def load_records(self):
        """Load records from a JSON file if it exists."""
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
        """Save the current records to a JSON file."""
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
        """Check whether id_value is unique among records of record_type."""
        for idx, rec in enumerate(self.records):
            if rec.get("Type") == record_type:
                if ignore_index is not None and idx == ignore_index:
                    continue
                if rec.get("ID") == id_value:
                    return False
        return True
      
    def main_menu():
        print("\n--- Travel Agent Record Management ---")
        print("1. Create Record")
        print("2. Delete Record")
        print("3. Update Record")
        print("4. Search and Display Record")
        print("5. Exit")

    def input_client() -> dict:
        name = input("Enter client name: ")
        addr1 = input("Enter Address Line 1: ")
        addr2 = input("Enter Address Line 2 (optional): ")
        addr3 = input("Enter Address Line 3 (optional): ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter Zip Code: ")
        country = input("Enter Country: ")
        phone = input("Enter Phone Number: ")
        return {
            "Type": "Client",
            "ID": None,
            "Name": name,
            "Address Line 1": addr1,
            "Address Line 2": addr2,
            "Address Line 3": addr3,
            "City": city,
            "State": state,
            "Zip Code": zip_code,
            "Country": country,
            "Phone Number": phone
        }

    def input_airline() -> dict:
        company_name = input("Enter Airline Company Name: ")
        return {
            "Type": "Airline",
            "ID": None,
            "Company Name": company_name
        }

    def input_flight() -> dict:
        try:
            client_id = int(input("Enter Client ID: "))
            airline_id = int(input("Enter Airline ID: "))
        except ValueError:
            print("Client ID and Airline ID must be integers.")
            return None
        date_str = input("Enter Date (YYYY-MM-DD HH:MM): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d HH:MM")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD HH:MM.")
            return None
        start_city = input("Enter Start City: ")
        end_city = input("Enter End City: ")
        return {
            "Type": "Flight",
            "Client_ID": client_id,
            "Airline_ID": airline_id,
            "Date": date_str,
            "Start City": start_city,
            "End City": end_city
        }
def display_records(records):
    if not records:
        print("No records found.")
    else:
        for rec in records:
            for key, value in rec.items():
                print(f"{key}: {value}")
            print("-" * 40)
            
            
def get_client_by_id(manager: RecordManager, client_id: int):
    """Return the Client record that has the given ID."""
    for rec in manager.records:
        if rec.get("Type") == "Client" and rec.get("ID") == client_id:
            return rec
    return None

def get_airline_by_id(manager: RecordManager, airline_id: int):
    """Return the Airline record that has the given ID."""
    for rec in manager.records:
        if rec.get("Type") == "Airline" and rec.get("ID") == airline_id:
            return rec
    return None

  
class RecordManager:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = file_name
        self.records = []  # Internal storage as a list of dictionaries.
        self.load_records()

    def add_record(self, record: dict):
        if record.get("Type") in ("Client", "Airline"):
            if record.get("ID") is None or not self.is_unique_id(record["Type"], record["ID"]):
                record["ID"] = self.generate_id(record["Type"])
        self.records.append(record)

    def delete_record(self, record: dict):
        try:
            self.records.remove(record)
            return True
        except ValueError:
            return False

    def update_record(self, index: int, new_record: dict):
        if self.records[index].get("Type") in ("Client", "Airline"):
            if new_record.get("ID") != self.records[index].get("ID"):
                if not self.is_unique_id(new_record["Type"], new_record.get("ID"), ignore_index=index):
                    print("Error: The provided ID is not unique. Update aborted.")
                    return False
        self.records[index] = new_record
        return True

    def search_records(self, record_type: str, search_key: str, search_value: str):
        results = []
        for rec in self.records:
            if rec.get("Type") == record_type:
                if str(rec.get(search_key, "")).lower() == str(search_value).lower():
                    results.append(rec)
        return results



if __name__ == '__main__':
    main_menu()
