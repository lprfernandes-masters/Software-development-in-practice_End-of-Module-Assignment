import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
from .create_forms import *
from .update_forms import *


class RecordManagementGUI:
    def __init__(self, root, record_manager, save_callback):
        self.root = root
        self.record_manager = record_manager
        self.save_callback = save_callback
        self.current_record_type = "Client"
        self.displayed_records = []  # holds all records currently shown in the listbox
        self.setup_ui()

    def setup_ui(self):
        self.root.title("RoamWide Travels: Record Management System")
        self.root.configure(background="white")
        self.root.geometry("1200x800")

        # Sidebar for record type selection (affects creation type only).
        self.sidebar = tk.Frame(self.root, width=300, bg="#38b6ff")
        self.sidebar.pack(side="left", fill="y")

        tk.Button(
            self.sidebar,
            text="Client Record",
            font=("Times New Roman", 14, "bold"),
            command=lambda: self.set_current_record_type("Client")
        ).pack(pady=10, padx=10, fill="x")
        tk.Button(
            self.sidebar,
            text="Airline Record",
            font=("Times New Roman", 14, "bold"),
            command=lambda: self.set_current_record_type("Airline")
        ).pack(pady=10, padx=10, fill="x")
        tk.Button(
            self.sidebar,
            text="Flight Record",
            font=("Times New Roman", 14, "bold"),
            command=lambda: self.set_current_record_type("Flight")
        ).pack(pady=10, padx=10, fill="x")

        # Main area for CRUD operations.
        self.main_area = tk.Frame(self.root, bg="white")
        self.main_area.pack(side="right", expand=True, fill="both")

        # Button frame.
        self.button_frame = tk.Frame(self.main_area, bg="white")
        self.button_frame.pack(pady=20)

        tk.Button(
            self.button_frame,
            text="Create Record",
            font=("Times New Roman", 14, "bold"),
            command=self.create_record
        ).pack(side="left", padx=10, pady=5, ipadx=10, ipady=5)
        tk.Button(
            self.button_frame,
            text="Update Record",
            font=("Times New Roman", 14, "bold"),
            command=self.update_record
        ).pack(side="left", padx=10, pady=5, ipadx=10, ipady=5)
        tk.Button(
            self.button_frame,
            text="Delete Record",
            font=("Times New Roman", 14, "bold"),
            command=self.delete_record
        ).pack(side="left", padx=10, pady=5, ipadx=10, ipady=5)
        tk.Button(
            self.button_frame,
            text="Search & Display",
            font=("Times New Roman", 14, "bold"),
            command=self.search_record
        ).pack(side="left", padx=10, pady=5, ipadx=10, ipady=5)

        # Listbox to display all records.
        self.records_listbox = tk.Listbox(self.main_area, width=80)
        self.records_listbox.pack(padx=10, pady=10, fill="both", expand=True)
        self.refresh_records()

    def set_current_record_type(self, record_type):
        self.current_record_type = record_type
        messagebox.showinfo("Record Type Selected",
                            f"Current record type set to {record_type}")
        self.refresh_records()

    def refresh_records(self):
        """Display all records in the listbox, regardless of type."""
        self.records_listbox.delete(0, tk.END)
        self.displayed_records = []
        for rec in self.record_manager.records:
            self.displayed_records.append(rec)
            self.records_listbox.insert(tk.END, str(rec))

    def create_record(self):
        if self.current_record_type == "Client":
            form_data = create_client_form(self.root)
            if not form_data:
                return
            record = {
                "Type": "Client",
                "Name": form_data["Name"],
                "Address Line 1": form_data["Address Line 1"],
                "Address Line 2": form_data["Address Line 2"],
                "Address Line 3": form_data["Address Line 3"],
                "City": form_data["City"],
                "State": form_data["State"],
                "Zip Code": form_data["Zip Code"],
                "Country": form_data["Country"],
                "Phone Number": form_data["Phone Number"]
            }
        elif self.current_record_type == "Airline":
            form_data = create_airline_form(self.root)
            if not form_data:
                return
            record = {
                "Type": "Airline",
                "Company Name": form_data["Company Name"]
            }
        elif self.current_record_type == "Flight":
            form_data = create_flight_form(self.root)
            if not form_data:
                return
            try:
                client_id = int(form_data["Client ID"])
                airline_id = int(form_data["Airline ID"])
            except ValueError:
                messagebox.showerror("Error", "Invalid ID for flight record.")
                return

            try:
                date_obj = datetime.strptime(
                    form_data["Date (DD-MM-YYYY)"], "%d-%m-%Y")
            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid date format. Use DD-MM-YYYY.")
                return

            # The date is saved in isoformat.
            record = {
                "Type": "Flight",
                "Client_ID": client_id,
                "Airline_ID": airline_id,
                "Date": date_obj.isoformat(),
                "Start City": form_data["Start City"],
                "End City": form_data["End City"]
            }
        else:
            messagebox.showerror("Error", "Unknown record type")
            return

        self.record_manager.add_record(record)
        self.refresh_records()
        messagebox.showinfo(
            "Success", f"{self.current_record_type} record created.")
        self.save_callback()

    def update_record(self):
        selection = self.records_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "No record selected")
            return

        record = self.displayed_records[selection[0]]
        rec_type = record.get("Type")

        if rec_type == "Client":
            client_record = {
                "name": record.get("Name", ""),
                "address_line1": record.get("Address Line 1", ""),
                "address_line2": record.get("Address Line 2", ""),
                "address_line3": record.get("Address Line 3", ""),
                "city": record.get("City", ""),
                "state": record.get("State", ""),
                "zip_code": record.get("Zip Code", ""),
                "country": record.get("Country", ""),
                "phone_number": record.get("Phone Number", "")
            }
            form_data = update_client_form(self.root, client_record)
            updated = {
                "Type": "Client",
                "ID": record.get("ID"),
                "Name": form_data["Name"],
                "Address Line 1": form_data["Address Line 1"],
                "Address Line 2": form_data["Address Line 2"],
                "Address Line 3": form_data["Address Line 3"],
                "City": form_data["City"],
                "State": form_data["State"],
                "Zip Code": form_data["Zip Code"],
                "Country": form_data["Country"],
                "Phone Number": form_data["Phone Number"]
            }
        elif rec_type == "Airline":
            airline_record = {
                "company_name": record.get("Company Name", "")
            }
            form_data = update_airline_form(self.root, airline_record)
            updated = {
                "Type": "Airline",
                "ID": record.get("ID"),
                "Company Name": form_data["Company Name"]
            }
        elif rec_type == "Flight":
            flight_record = {
                "airline_id": record.get("Airline_ID", ""),
                "date": datetime.fromisoformat(record.get("Date")).strftime("%d-%m-%Y") if record.get("Date") else "",
                "start_city": record.get("Start City", ""),
                "end_city": record.get("End City", "")
            }
            form_data = update_flight_form(self.root, flight_record)
            try:
                date_obj = datetime.strptime(
                    form_data["Date (DD-MM-YYYY)"], "%d-%m-%Y")
            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid date format. Use DD-MM-YYYY.")
                return
            updated = {
                "Type": "Flight",
                "Client_ID": record.get("Client_ID"),
                "Airline_ID": record.get("Airline_ID"),
                "Date": date_obj.isoformat(),
                "Start City": form_data["Start City"],
                "End City": form_data["End City"]
            }
        else:
            messagebox.showerror("Error", "Unknown record type")
            return

        try:
            actual_index = self.record_manager.records.index(record)
        except ValueError:
            messagebox.showerror("Error", "Record not found in records.")
            return

        self.record_manager.update_record(actual_index, updated)
        messagebox.showinfo("Success", f"{rec_type} record updated.")
        self.save_callback()
        self.refresh_records()

    def delete_record(self):
        selection = self.records_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "No record selected")
            return
        index = selection[0]
        record = self.displayed_records[index]
        if messagebox.askyesno("Confirm", "Delete this record?"):
            if self.record_manager.delete_record(record):
                self.refresh_records()
                messagebox.showinfo("Success", "Record deleted")
            else:
                messagebox.showerror("Error", "Deletion failed")

    def search_record(self):
        search_term = simpledialog.askstring("Search", "Enter search term:")
        if search_term is None:
            return
        results = []
        for rec in self.record_manager.records:
            if search_term.lower() in str(rec).lower():
                results.append(rec)
        if results:
            result_str = "\n".join(str(r) for r in results)
            messagebox.showinfo(
                "Search Results", f"Records found:\n{result_str}")
        else:
            messagebox.showinfo("Search Results", "No records found.")
