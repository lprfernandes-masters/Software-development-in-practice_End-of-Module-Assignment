import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Create a window
root = tk.Tk()

# Window details
root.title("RoamWide Travels: Record Management System")
root.configure(background="white")
root.geometry("2000x1000")

# Create Sidebar and main area for table and CRUD operations
sidebar = tk.Frame(root, width=300, background="blue")  
sidebar.pack(side="left", fill="y")
crud_buttons_area = tk.Frame(root, background="white")
crud_buttons_area.pack(side="right", expand=True, fill="both")

# Function to create Sidebar Buttons
def create_sidebar_button_client_record(text, record_type):
    btn = tk.Button(sidebar, text="Client Record", background="white", foreground="black", font=("Times New Roman", 14, "bold"), relief="solid",anchor="center", justify="center")   
    btn.pack(pady=10, padx=10, fill="x")

def create_sidebar_button_airline_record(text, record_type):
    btn = tk.Button(sidebar, text="Airline Record", background="white", foreground="black", font=("Times New Roman", 14, "bold"), relief="solid",anchor="center", justify="center")   
    btn.pack(pady=10, padx=10, fill="x")

def create_sidebar_button_flight_record(text, record_type):
    btn = tk.Button(sidebar, text="Flight Record", background="white", foreground="black", font=("Times New Roman", 14, "bold"), relief="solid",anchor="center", justify="center")
    btn.pack(pady=10, padx=10, fill="x")

# Call the functions to create buttons
create_sidebar_button_client_record("Client Record", "Client")
create_sidebar_button_airline_record("Airline Record", "Airline")
create_sidebar_button_flight_record("Flight Record", "Flight")

# Create frames for the area with CRUD buttons 
button_frame = tk.Frame(crud_buttons_area)
button_frame.pack(pady=20)

# Create buttons for CRUD with background colors
def create_crud_buttons_create_record(text, color):
    btn = tk.Button(button_frame, text="Create", highlightbackground="green", foreground="black", font=("Times New Roman", 14, "bold"), relief="raised")
    btn.pack(side="left", padx=10, pady=5, ipadx=10, ipady=5)
def create_crud_buttons_delete_record(text, color):
    btn = tk.Button(button_frame, text="Delete", highlightbackground="orange", foreground="black", font=("Times New Roman", 14, "bold"), relief="raised")
    btn.pack(side="left", padx=10, pady=5, ipadx=10, ipady=5)
def create_crud_buttons_update_record(text, color):
    btn = tk.Button(button_frame, text="Update", highlightbackground="pink", foreground="black", font=("Times New Roman", 14, "bold"), relief="raised")
    btn.pack(side="left", padx=10, pady=5, ipadx=10, ipady=5)
def create_crud_buttons_search_display_record(text, color):
    btn = tk.Button(button_frame, text="Search&Display", highlightbackground="blue", foreground="black", font=("Times New Roman", 14, "bold"), relief="raised")
    btn.pack(side="left", padx=10, pady=5, ipadx=10, ipady=5)

# Call function to create CRUD buttons with specified background colors 
create_crud_buttons_create_record("Create a Record", "green")  
create_crud_buttons_delete_record("Delete a Record", "orange") 
create_crud_buttons_update_record("Update a Record", "red") 
create_crud_buttons_search_display_record("Search & Display", "blue") 


root.mainloop()
