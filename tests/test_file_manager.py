import os
import unittest
from src.services.file_manager import load_records, save_records


class TestFileManager(unittest.TestCase):
    test_file = "test_records.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load(self):
        records = [{"ID": 1, "Type": "Client", "Name": "Someone"}]
        save_records(records, self.test_file)
        loaded = load_records(self.test_file)
        self.assertEqual(records, loaded)


if __name__ == '__main__':
    unittest.main()
