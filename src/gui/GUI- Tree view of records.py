import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Sample data to populate the Treeview
records = [
    {'ID': 1, 'Type': 'Client', 'Name': 'John Doe', 'City': 'New York', 'Phone Number': '123-456-7890'},
    {'ID': 2, 'Type': 'Client', 'Name': 'Jane Smith', 'City': 'Los Angeles', 'Phone Number': '987-654-3210'},
    {'ID': 3, 'Type': 'Airline', 'Company Name': 'Delta Airlines'},
    {'ID': 4, 'Type': 'Flight', 'Client_ID': 1, 'Airline_ID': 3, 'Start City': 'New York', 'End City': 'Los Angeles'},
]


def display_records():
    # New window to show records
    records_window = tk.Toplevel()
    records_window.title("Records Display")

    # Treeview to display the records
    tree = ttk.Treeview(records_window)

    # Columns for the Treeview
    tree["columns"] = ("ID", "Type", "Name", "City", "Phone Number")
    tree["show"] = "headings"  # This hides the default first column (index)

    # The headings (column names)
    tree.heading("ID", text="ID")
    tree.heading("Type", text="Type")
    tree.heading("Name", text="Name")
    tree.heading("City", text="City")
    tree.heading("Phone Number", text="Phone Number")

    # Adding data to the records
    for record in records:
        tree.insert("", tk.END, values=(record.get('ID', ''), record.get('Type', ''),
                                        record.get('Name', ''), record.get('City', ''),
                                        record.get('Phone Number', '')))

    # Adding a scrollbar
    tree_scroll = ttk.Scrollbar(records_window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=tree_scroll.set)
    tree_scroll.pack(side="right", fill="y")
    tree.pack(padx=20, pady=20)


# Main menu function
def main_menu():
    window = tk.Tk()
    window.title("Record Management System")

    # Button to display the records
    display_button = tk.Button(window, text="Display Records", command=display_records)
    display_button.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main_menu()