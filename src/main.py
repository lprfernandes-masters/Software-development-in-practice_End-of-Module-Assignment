import tkinter as tk
from tkinter import messagebox
from services.file_manager import load_records, save_records
from services.record_manager import RecordManager
from gui.gui import RecordManagementGUI


def main_menu():
    record_manager = RecordManager()

    root = tk.Tk()

    # https://stackoverflow.com/questions/66668898/retrieve-get-back-command-callback-function-from-tkinter-widget
    RecordManagementGUI(root, record_manager,
                        save_callback=lambda: save_records(record_manager.records))

    def close_app():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            save_records(record_manager.records)
            root.destroy()

    # close window event triggers close_app function.
    # https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter
    root.protocol("WM_DELETE_WINDOW", close_app)
    root.mainloop()


if __name__ == '__main__':
    main_menu()
