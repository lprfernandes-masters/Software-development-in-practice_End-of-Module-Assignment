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
        if self.records[index].get("Type") in ("Client", "Airline"):
            if new_record.get("ID") != self.records[index].get("ID"):
                if not self.is_unique_id(new_record["Type"], new_record.get("ID"), ignore_index=index):
                    print("Error: The provided ID is not unique. Update aborted.")
                    return False
        self.records[index] = new_record
        save_records(self.records)
        return True

    def search_records(self, record_type: str, search_key: str, search_value: str):
        """
        Generic search for Client or Airline records by matching key/value (case-insensitive).
        """
        results = []
        for rec in self.records:
            if rec.get("Type") == record_type:
                if str(rec.get(search_key, "")).lower() == str(search_value).lower():
                    results.append(rec)
        return results

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
