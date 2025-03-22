import unittest
from unittest.mock import patch as mock
from src.services.record_manager import RecordManager


class TestRecordManager(unittest.TestCase):

    def setUp(self):
        # mocking load records to return always empty (patching the local ref of record_manager)
        load_mock = mock(
            'src.services.record_manager.load_records', return_value=[])
        self.mock_load = load_mock.start()
        self.addCleanup(load_mock.stop)

        # mocking saving records to avoid file I/O. (patching the local ref of record_manager)
        save_mock = mock('src.services.record_manager.save_records')
        self.mock_save = save_mock.start()
        self.addCleanup(save_mock.stop)

        # a new RecordManager instance for each test.
        self.record_manager = RecordManager()

    def test_add_record_client_assigns_id(self):
        # Expect the first generated ID to be 1.
        record = {"Type": "Client", "Name": "Alice", "ID": None}

        self.record_manager.add_record(record)

        self.assertIsNotNone(record.get("ID"))
        self.assertEqual(record["ID"], 1)
        self.assertIn(record, self.record_manager.records)
        self.mock_save.assert_called()

    def test_add_record_airline_assigns_id(self):
        """For an Airline record, if ID is None, it should be auto-assigned."""

        record = {"Type": "Airline", "Company Name": "AirTest", "ID": None}
        self.record_manager.add_record(record)
        self.assertIsNotNone(record.get("ID"))
        self.assertEqual(record["ID"], 1)
        self.assertIn(record, self.record_manager.records)
        self.mock_save.assert_called()

    def test_add_record_flight_does_not_assign_id(self):
        """Flight records should not have an ID assigned."""

        record = {"Type": "Flight", "Client_ID": 1, "Airline_ID": 2,
                  "Date": "01-01-2000", "Start City": "City1", "End City": "City2"}
        self.record_manager.add_record(record)
        self.assertNotIn("ID", record)
        self.assertIn(record, self.record_manager.records)
        self.mock_save.assert_called()

    def test_update_record(self):
        """Adds and then updates the record"""
        record = {"Type": "Client", "ID": 1, "Name": "Luis"}

        self.record_manager.records.append(record)
        new_record = {"Type": "Client", "ID": 1, "Name": "Luis Updated"}
        result = self.record_manager.update_record(0, new_record)
        self.assertTrue(result)
        self.assertEqual(
            self.record_manager.records[0]["Name"], "Luis Updated")
        self.mock_save.assert_called()

    def test_delete_record_success(self):
        """Adds and then deletes a record."""
        record = {"Type": "Client", "ID": 1, "Name": "Luis"}

        self.record_manager.records.append(record)
        result = self.record_manager.delete_record(record)
        self.assertTrue(result)
        self.assertNotIn(record, self.record_manager.records)
        self.mock_save.assert_called()

    def test_delete_record_failure(self):
        """Deleting a non existent record should return False."""
        record = {"Type": "Client", "ID": 1, "Name": "Elnara"}

        result = self.record_manager.delete_record(record)
        self.assertFalse(result)
        # Here we should not call save_records.
        self.mock_save.assert_not_called()

    def test_generate_id(self):
        # generate_id should return 1 for client ids.
        new_id = self.record_manager.generate_id("Client")
        self.assertEqual(new_id, 1)

        # If 1 is observed we should have the 2 for client ids.
        self.record_manager.records.append({"Type": "Client", "ID": 1})
        new_id = self.record_manager.generate_id("Client")
        self.assertEqual(new_id, 2)

        # Same for Airline records. It should return maxid + 1
        self.record_manager.records.append({"Type": "Airline", "ID": 5})
        new_id = self.record_manager.generate_id("Airline")
        self.assertEqual(new_id, 6)

        # For a record type with no records, it should return 1.
        new_id = self.record_manager.generate_id("NonExistent")
        self.assertEqual(new_id, 1)


if __name__ == '__main__':
    unittest.main()
