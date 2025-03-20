import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Sample client data to test the treeview
records = [
    {'ID': 1, 'Type': 'Client', 'Name': 'April Smith', 'City': 'Geneva', 'Phone Number': '573-384-3983'},
    {'ID': 2, 'Type': 'Client', 'Name': 'Sakura Yamashita', 'City': 'Tokyo', 'Phone Number': '112-3783-8723'}
]

def display_records():
    records_window = tk.Toplevel()
    records_window.title("Records Display")

    # Treeview to show the records
    tree = ttk.Treeview(records_window)

    # Columns for the Treeview
    tree["columns"] = ("ID", "Type", "Name", "City", "Phone Number")
    tree["show"] = "headings"  # This hides the default first column (index)

    # Defining the headings of the column
    tree.heading("ID", text="ID")
    tree.heading("Type", text="Type")
    tree.heading("Name", text="Name")
    tree.heading("City", text="City")
    tree.heading("Phone Number", text="Phone Number")

    # This is to add data to the Treeview (client records, airline records and flight records)
    for record in records:
        tree.insert("", tk.END, values=(record.get('ID', ''), record.get('Type', ''),
                                        record.get('Name', ''), record.get('City', ''),
                                        record.get('Phone Number', '')))

    # For scrollbar
    tree_scroll = ttk.Scrollbar(records_window, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=tree_scroll.set)
    tree_scroll.pack(side="right", fill="y")
    tree.pack(padx=20, pady=20)

# Function to update the appearance of ttk widgets
def style_widgets():
    style = ttk.Style()

    # To set the theme
    style.theme_use('classic')  # You can try 'alt', 'clam', 'classic', 'vista', 'xpnative', etc.

    # Button Style
    style.configure("TButton",
                    font=("Segoe UI", 12),
                    padding=6,
                    relief="flat",
                    background= "#1c61ad",  # Company dark blue color
                    foreground="white")

    style.map("TButton",
              background=[('active', None), ('pressed', None)],
              foreground=[('active', 'black')])

    # Define the sidebarButton style
    style.configure("SidebarButton",
                    font=("Segoe UI", 12),
                    padding=10,
                    relief="flat",
                    background="#2e3b4e",
                    foreground="white")

    style.map("SidebarButton",
              background=[('active', '#35526d'), ('pressed', '#2c3e50')],
              foreground=[('active', 'white')])


    # Label Style
    style.configure("TLabel",
                    font=("Segoe UI", 12),
                    background="#f1f1f1",
                    foreground="#333")

    # Entry Style
    style.configure("TEntry",
                    font=("Segoe UI", 12),
                    padding=5)

    # Treeview Style
    style.configure("Treeview",
                    font=("Segoe UI", 12),
                    background="#f9f9f9",
                    foreground="black",
                    rowheight=30)

    style.configure("Treeview.Heading",
                    font=("Segoe UI", 14, 'bold'),
                    background="#38b6ff",  # Company Blue Color
                    foreground="white")

# Sidebar layout with buttons
def create_sidebar(window):
    sidebar_frame = tk.Frame(window, bg="#38b6ff", width=200,)
    sidebar_frame.pack(side="left", fill="y", anchor="n")

    # This adds the company logo to the sidebar
    logo = Image.open(
        "/Users/reginaportuondo/Downloads/End-of-Module-Assignment/Roamwidetravel2 .png")
    logo = logo.resize((200, 200))
    logo_img = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(sidebar_frame, image=logo_img, bg="#38b6ff")  # This blends in the image background with sidebar
    logo_label.image = logo_img  # Reference to the image
    logo_label.pack(pady=10)

    client_icon = Image.open("/Users/reginaportuondo/Downloads/End-of-Module-Assignment/client.png").resize((20, 20))
    client_icon = ImageTk.PhotoImage(client_icon)


    # Sidebar Buttons
    ttk.Button(sidebar_frame, text="Client Records", command=client_management, style="SidebarButton.TButton").pack(pady=10,
                                                                                                            fill="x")
    ttk.Button(sidebar_frame, text="Flight Records", command=flight_management, style="SidebarButton.TButton").pack(pady=10,
                                                                                                            fill="x")
    ttk.Button(sidebar_frame, text="Airline Records", command=airline_management, style="SidebarButton.TButton").pack(pady=10,
                                                                                                                    fill="x")
# Update Client Record Function
def update_client():
    update_window = tk.Toplevel()
    update_window.title("Update Client Record")

    # Here the user can select a record to update (using a drop-down)
    client_names = [record['Name'] for record in records if record['Type'] == 'Client']

    # Dropdown to select client for updating
    selected_client = tk.StringVar()
    client_dropdown = tk.OptionMenu(update_window, selected_client, *client_names)
    client_dropdown.pack(pady=10)

    # This is to create entry fields for Name and City
    tk.Label(update_window, text="Client Name").pack()
    client_name_entry = tk.Entry(update_window)
    client_name_entry.pack(pady=5)

    tk.Label(update_window, text="Client City").pack()
    client_city_entry = tk.Entry(update_window)
    client_city_entry.pack(pady=5)

    # Fetch selected client data when user selects a client
    def fetch_client_data():
        selected_client_name = selected_client.get()
        # Find the selected client record
        client_record = next((r for r in records if r['Type'] == 'Client' and r['Name'] == selected_client_name), None)
        if client_record:
            client_name_entry.delete(0, tk.END)
            client_name_entry.insert(0, client_record['Name'])
            client_city_entry.delete(0, tk.END)
            client_city_entry.insert(0, client_record['City'])
        else:
            messagebox.showerror("Error", "Client not found!")

    # Button to fetch the client data
    fetch_button = tk.Button(update_window, text="Fetch Client Data", command=fetch_client_data)
    fetch_button.pack(pady=10)

    # Button to update the client record
    def update_client_data():
        # Get the updated values from the entry fields
        new_name = client_name_entry.get()
        new_city = client_city_entry.get()

        # This is to find the client record to update
        selected_client_name = selected_client.get()
        client_record = next((r for r in records if r['Type'] == 'Client' and r['Name'] == selected_client_name), None)

        if client_record:
            client_record['Name'] = new_name
            client_record['City'] = new_city
            messagebox.showinfo("Success", f"Client {new_name} updated successfully!")
            update_window.destroy()
        else:
            messagebox.showerror("Error", "Client not found!")

    # Update Button
    tk.Button(update_window, text="Update Client", command=update_client_data).pack(pady=10)

# Delete Client Record Function
def delete_client():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Client Record")

    # Dropdown to select client for deletion
    client_names = [record['Name'] for record in records if record['Type'] == 'Client']

    selected_client = tk.StringVar()
    client_dropdown = tk.OptionMenu(delete_window, selected_client, *client_names)
    client_dropdown.pack(pady=10)

    # Button to delete the selected client
    def delete_client_data():
        selected_client_name = selected_client.get()
        # to find the client record to delete
        client_record = next((r for r in records if r['Type'] == 'Client' and r['Name'] == selected_client_name), None)

        if client_record:
            records.remove(client_record)
            messagebox.showinfo("Success", f"Client {selected_client_name} deleted successfully!")
            delete_window.destroy()
        else:
            messagebox.showerror("Error", "Client not found!")

    # Delete Button
    tk.Button(delete_window, text="Delete Client", command=delete_client_data).pack(pady=10)

# Search Client Record Function
def search_client():
    search_window = tk.Toplevel()
    search_window.title("Search Client Record")

    # The entry field to search by name
    tk.Label(search_window, text="Enter Client Name to Search").pack(pady=10)
    search_entry = tk.Entry(search_window)
    search_entry.pack(pady=10)

    # To display search results in a Treeview
    result_tree = ttk.Treeview(search_window, columns=("ID", "Type", "Name", "City"), show="headings")
    result_tree.heading("ID", text="ID")
    result_tree.heading("Type", text="Type")
    result_tree.heading("Name", text="Name")
    result_tree.heading("City", text="City")

    # Search Button
    def search_action():
        query = search_entry.get().lower()
        if query:
            # To filter records by client name
            filtered_records = [r for r in records if r['Type'] == 'Client' and query in r['Name'].lower()]
            for row in result_tree.get_children():
                result_tree.delete(row)
            for record in filtered_records:
                result_tree.insert("", tk.END, values=(record['ID'], record['Type'], record['Name'], record['City']))
        else:
            messagebox.showwarning("Warning", "Please enter a name to search!")

    tk.Button(search_window, text="Search", command=search_action).pack(pady=10)
    result_tree.pack(pady=20)


# Create Client Form
def create_client():
    create_window = tk.Toplevel()
    create_window.title("Create Client Record")

    # Apply styling to widgets
    style_widgets()

    # Background color for the window is currently white
    create_window.config(bg="#f1f1f1")

    # Labels and Entry fields
    tk.Label(create_window, text="Client Name", style="TLabel", background="#f1f1f1").grid(row=0, column=0, padx=20,
                                                                                           pady=10, sticky="w")
    client_name_entry = ttk.Entry(create_window, style="TEntry")
    client_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

    tk.Label(create_window, text="City", style="TLabel", background="#f1f1f1").grid(row=1, column=0, padx=20, pady=10,
                                                                                    sticky="w")
    client_city_entry = ttk.Entry(create_window, style="TEntry")
    client_city_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

    # Submit Button
    def submit_client():
        new_client = {
            'ID': len(records) + 1,
            'Type': 'Client',
            'Name': client_name_entry.get(),
            'City': client_city_entry.get(),
            'Phone Number': 'Not Provided'
        }
        records.append(new_client)
        messagebox.showinfo("Success", f"Client {new_client['Name']} created successfully!")
        create_window.destroy()

    ttk.Button(create_window, text="Submit", command=submit_client).grid(row=2, column=0, columnspan=2, pady=20)

# Main menu window
def main_menu():
    window = tk.Tk()
    window.title("RoamWide Travel Record Management System")
    window.geometry("800x600")
    window.config(bg="#f1f1f1")

    # Option for border at the top of the window
    #top_border_frame = tk.Frame(window, bg="#38b6ff", height=20)
    #top_border_frame.pack(side="top", fill="x")

    # Apply styling to widgets
    style_widgets()

    # Option to company logo in window
    #add_logo(window)

    # Create Sidebar
    create_sidebar(window)

    # Main content area
    content_frame = tk.Frame(window, bg="#f1f1f1")
    content_frame.pack(side="right", fill="both", expand=True)

    window.mainloop()


# Client Management Window
def client_management():
    client_window = tk.Toplevel()
    client_window.title("Client Record Management")
    client_window.config(bg="#f1f1f1")

    # Apply styling
    style_widgets()

    # Buttons for client record operations
    ttk.Button(client_window, text="Create Client", command=create_client).pack(pady=10, fill="x", padx=40)
    ttk.Button(client_window, text="Display Records", command=display_records).pack(pady=10, fill="x", padx=40)
    #display_button = tk.Button(client_window, text="Display Records", command=display_records)
    #(display_button.pack(pady=10, fill="x", padx=40))
    ttk.Button(client_window, text="Search Client", command=search_client).pack(pady=10, fill="x", padx=40)
    ttk.Button(client_window, text="Delete Client", command=delete_client).pack(pady=10, fill="x", padx=40)
    ttk.Button(client_window, text="Update Client", command=update_client).pack(pady=10, fill="x", padx=40)



# Sample flight and airline management windows
def flight_management():
    flight_window = tk.Toplevel()
    flight_window.title("Flight Record Management")
    flight_window.config(bg="#f1f1f1")

    ttk.Button(flight_window, text="Create Flight", command=create_client).pack(pady=10, fill="x", padx=40)
    ttk.Button(flight_window, text="Update Flight", command=create_client).pack(pady=10, fill="x", padx=40)


def airline_management():
    airline_window = tk.Toplevel()
    airline_window.title("Airline Record Management")
    airline_window.config(bg="#f1f1f1")

    ttk.Button(airline_window, text="Create Airline", command=create_client).pack(pady=10, fill="x", padx=40)
    ttk.Button(airline_window, text="Update Airline", command=create_client).pack(pady=10, fill="x", padx=40)



if __name__ == "__main__":
    main_menu()