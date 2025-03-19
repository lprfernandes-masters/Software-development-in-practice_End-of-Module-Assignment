
from datetime import datetime


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


def search_flight_menu(manager: RecordManager):
    print("\nSearch Flight Records by:")
    print("1. Client Name")
    print("2. Airline Name")
    print("3. Client ID")
    print("4. Airline ID")
    print("5. Date")
    option = input("Enter your option: ").strip()
    results = []

    if option == "1":
        search_val = input("Enter Client Name: ").strip().lower()
        for rec in manager.records:
            if rec.get("Type") == "Flight":
                client = get_client_by_id(manager, rec.get("Client_ID"))
                if client and client.get("Name", "").lower() == search_val:
                    results.append(rec)
    elif option == "2":
        search_val = input("Enter Airline Name: ").strip().lower()
        for rec in manager.records:
            if rec.get("Type") == "Flight":
                airline = get_airline_by_id(manager, rec.get("Airline_ID"))
                if airline and airline.get("Company Name", "").lower() == search_val:
                    results.append(rec)
    elif option == "3":
        try:
            search_val = int(input("Enter Client ID: "))
        except ValueError:
            print("Invalid Client ID. Must be an integer.")
            return
        for rec in manager.records:
            if rec.get("Type") == "Flight" and rec.get("Client_ID") == search_val:
                results.append(rec)
    elif option == "4":
        try:
            search_val = int(input("Enter Airline ID: "))
        except ValueError:
            print("Invalid Airline ID. Must be an integer.")
            return
        for rec in manager.records:
            if rec.get("Type") == "Flight" and rec.get("Airline_ID") == search_val:
                results.append(rec)
    elif option == "5":
        search_val = input("Enter Date (YYYY-MM-DD HH:MM): ").strip()
        for rec in manager.records:
            if rec.get("Type") == "Flight" and rec.get("Date") == search_val:
                results.append(rec)
    else:
        print("Invalid option.")
        return

    if results:
        display_records(results)
    else:
        print("No matching flight records found.")


def create_menu(manager: RecordManager):
    print("\n--- Create Record ---")
    print("a. Client Record")
    print("b. Airline Record")
    print("c. Flight Record")
    choice = input("Enter your choice (a/b/c): ").strip().lower()
    if choice == 'a':
        record = input_client()
        manager.add_record(record)
        print("Client record created.")
    elif choice == 'b':
        record = input_airline()
        manager.add_record(record)
        print("Airline record created.")
    elif choice == 'c':
        record = input_flight()
        if record:
            manager.add_record(record)
            print("Flight record created.")
    else:
        print("Invalid option.")


def delete_menu(manager: RecordManager):
    print("\n--- Delete Record ---")
    print("a. Client Record")
    print("b. Airline Record")
    print("c. Flight Record")
    choice = input("Enter your choice (a/b/c): ").strip().lower()
    if choice in ('a', 'b'):
        rec_type = "Client" if choice == 'a' else "Airline"
        try:
            rec_id = int(input("Enter the record ID to delete: "))
        except ValueError:
            print("Invalid ID. Must be an integer.")
            return
        results = manager.search_records(rec_type, "ID", rec_id)
        if results:
            display_records(results)
            confirm = input(
                "Are you sure you want to delete this record? (y/n): ").strip().lower()
            if confirm == 'y':
                if manager.delete_record(results[0]):
                    print("Record deleted.")
                else:
                    print("Error deleting record.")
        else:
            print("Record not found.")
    elif choice == 'c':
        try:
            client_id = int(input("Enter Client ID: "))
            airline_id = int(input("Enter Airline ID: "))
        except ValueError:
            print("IDs must be integers.")
            return
        date_str = input("Enter Date (YYYY-MM-DD HH:MM): ")
        found = None
        for rec in manager.records:
            if rec.get("Type") == "Flight":
                if rec.get("Client_ID") == client_id and rec.get("Airline_ID") == airline_id and rec.get("Date") == date_str:
                    found = rec
                    break
        if found:
            display_records([found])
            confirm = input(
                "Are you sure you want to delete this flight record? (y/n): ").strip().lower()
            if confirm == 'y':
                if manager.delete_record(found):
                    print("Flight record deleted.")
                else:
                    print("Error deleting record.")
        else:
            print("Flight record not found.")
    else:
        print("Invalid option.")


def update_menu(manager: RecordManager):
    print("\n--- Update Record ---")
    print("a. Client Record")
    print("b. Airline Record")
    print("c. Flight Record")
    choice = input("Enter your choice (a/b/c): ").strip().lower()
    if choice in ('a', 'b'):
        rec_type = "Client" if choice == 'a' else "Airline"
        try:
            rec_id = int(input("Enter the record ID to update: "))
        except ValueError:
            print("Invalid ID. Must be an integer.")
            return
        results = manager.search_records(rec_type, "ID", rec_id)
        if results:
            print("Existing record:")
            display_records(results)
            if rec_type == "Client":
                print("Enter new values for the client record:")
                new_record = input_client()
            else:
                print("Enter new values for the airline record:")
                new_record = input_airline()
            new_record["ID"] = rec_id  # Preserve original ID.
            index = manager.records.index(results[0])
            if manager.update_record(index, new_record):
                print("Record updated.")
            else:
                print("Error updating record.")
        else:
            print("Record not found.")
    elif choice == 'c':
        try:
            client_id = int(input("Enter Client ID of the flight record: "))
            airline_id = int(input("Enter Airline ID of the flight record: "))
        except ValueError:
            print("IDs must be integers.")
            return
        date_str = input(
            "Enter Date (YYYY-MM-DD HH:MM) of the flight record: ")
        found = None
        for rec in manager.records:
            if rec.get("Type") == "Flight":
                if rec.get("Client_ID") == client_id and rec.get("Airline_ID") == airline_id and rec.get("Date") == date_str:
                    found = rec
                    break
        if found:
            print("Existing flight record:")
            display_records([found])
            print("Enter new details for the flight record:")
            new_record = input_flight()
            if new_record:
                index = manager.records.index(found)
                if manager.update_record(index, new_record):
                    print("Flight record updated.")
                else:
                    print("Error updating record.")
        else:
            print("Flight record not found.")
    else:
        print("Invalid option.")


def search_menu(manager: RecordManager):
    print("\n--- Search and Display Record ---")
    print("a. Client Record")
    print("b. Airline Record")
    print("c. Flight Record")
    choice = input("Enter your choice (a/b/c): ").strip().lower()
    if choice in ('a', 'b'):
        rec_type = "Client" if choice == 'a' else "Airline"
        key = input("Enter the field to search by (e.g., ID, Name): ").strip()
        value = input("Enter the search value: ").strip()
        if key.lower() == "id":
            try:
                value = int(value)
            except ValueError:
                print("ID must be an integer.")
                return
        results = manager.search_records(rec_type, key, value)
        display_records(results)
    elif choice == 'c':
        search_flight_menu(manager)
    else:
        print("Invalid option.")


def main_menu():
    manager = RecordManager()
    while True:
        print("\n--- Travel Agent Record Management ---")
        print("1. Create Record")
        print("2. Delete Record")
        print("3. Update Record")
        print("4. Search and Display Record")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            create_menu(manager)
        elif choice == '2':
            delete_menu(manager)
        elif choice == '3':
            update_menu(manager)
        elif choice == '4':
            search_menu(manager)
        elif choice == '5':
            manager.save_records()  # Save records before exiting.
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == '__main__':
    main_menu()
