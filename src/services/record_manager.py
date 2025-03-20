from services.file_manager import load_records, save_records


class RecordManager:
    def __init__(self):
        self.records = load_records()

    def add_record(self, record: dict):
        """Add a new record. For Client and Airline records, ensure a unique ID."""
        if record.get("Type") in ("Client", "Airline"):
            if record.get("ID") is None or not self.is_unique_id(record["Type"], record["ID"]):
                record["ID"] = self.generate_id(record["Type"])
        self.records.append(record)
        save_records(self.records)

    def delete_record(self, record: dict):
        """Delete the specified record."""
        try:
            self.records.remove(record)
            save_records(self.records)
            return True
        except ValueError:
            return False

    def update_record(self, index: int, new_record: dict):
        """
        Update a record at the given index. 
        Ensure new IDs are unique for Client and Airline records.
        """
        self.records[index] = new_record
        save_records(self.records)
        return True


    def generate_id(self, record_type: str):
        """Generate a new unique ID for a given record type ('Client' or 'Airline')."""
        ids = [rec["ID"] for rec in self.records
               if rec.get("Type") == record_type and rec.get("ID") is not None]
        return max(ids, default=0) + 1


    def get_client_by_id(self, client_id: int):
        for rec in self.records:
            if rec.get("Type") == "Client" and rec.get("ID") == client_id:
                return rec
        return None

    def get_airline_by_id(self, airline_id: int):
        for rec in self.records:
            if rec.get("Type") == "Airline" and rec.get("ID") == airline_id:
                return rec
        return None

    def get_flight_by_client_id(self, client_id: int):
        for rec in self.records:
            if rec.get("Type") == "Flight" and rec.get("Client_ID") == client_id:
                return rec
        return None
