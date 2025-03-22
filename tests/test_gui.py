
import unittest
import tkinter as tk
from src.gui.gui import RecordManagementGUI
from src.services.record_manager import RecordManager


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.rm = RecordManager()
        self.app = RecordManagementGUI(
            self.root, self.rm, save_callback=lambda: None)

    def tearDown(self):
        self.root.destroy()

    def test_widgets_exist(self):
        # Check if the window has built the buttons
        children = self.root.winfo_children()
        self.assertTrue(len(children) > 0)


if __name__ == '__main__':
    unittest.main()
