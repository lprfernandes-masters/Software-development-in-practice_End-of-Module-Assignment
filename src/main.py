import json
import os
from datetime import datetime

FILE_NAME = 'records.json'

def main_menu():
    print("\n--- Travel Agent Record Management ---")
    print("1. Create Record")
    print("2. Delete Record")
    print("3. Update Record")
    print("4. Search and Display Record")
    print("5. Exit")
    # (CLI commands will be integrated later)
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
