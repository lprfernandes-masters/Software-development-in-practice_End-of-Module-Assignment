import tkinter as tk


def create_client_form(root):
    form = tk.Toplevel(root)
    form.title("Create Client Record")
    form.grab_set()
    entries = {}

    tk.Label(form, text="Name").grid(
        row=0, column=0, padx=10, pady=5, sticky="e")
    name_entry = tk.Entry(form, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    entries["Name"] = name_entry

    tk.Label(form, text="Address Line 1").grid(
        row=1, column=0, padx=10, pady=5, sticky="e")
    addr1_entry = tk.Entry(form, width=30)
    addr1_entry.grid(row=1, column=1, padx=10, pady=5)
    entries["Address Line 1"] = addr1_entry

    tk.Label(form, text="Address Line 2").grid(
        row=2, column=0, padx=10, pady=5, sticky="e")
    addr2_entry = tk.Entry(form, width=30)
    addr2_entry.grid(row=2, column=1, padx=10, pady=5)
    entries["Address Line 2"] = addr2_entry

    tk.Label(form, text="Address Line 3").grid(
        row=3, column=0, padx=10, pady=5, sticky="e")
    addr3_entry = tk.Entry(form, width=30)
    addr3_entry.grid(row=3, column=1, padx=10, pady=5)
    entries["Address Line 3"] = addr3_entry

    tk.Label(form, text="City").grid(
        row=4, column=0, padx=10, pady=5, sticky="e")
    city_entry = tk.Entry(form, width=30)
    city_entry.grid(row=4, column=1, padx=10, pady=5)
    entries["City"] = city_entry

    tk.Label(form, text="State").grid(
        row=5, column=0, padx=10, pady=5, sticky="e")
    state_entry = tk.Entry(form, width=30)
    state_entry.grid(row=5, column=1, padx=10, pady=5)
    entries["State"] = state_entry

    tk.Label(form, text="Zip Code").grid(
        row=6, column=0, padx=10, pady=5, sticky="e")
    zip_entry = tk.Entry(form, width=30)
    zip_entry.grid(row=6, column=1, padx=10, pady=5)
    entries["Zip Code"] = zip_entry

    tk.Label(form, text="Country").grid(
        row=7, column=0, padx=10, pady=5, sticky="e")
    country_entry = tk.Entry(form, width=30)
    country_entry.grid(row=7, column=1, padx=10, pady=5)
    entries["Country"] = country_entry

    tk.Label(form, text="Phone Number").grid(
        row=8, column=0, padx=10, pady=5, sticky="e")
    phone_entry = tk.Entry(form, width=30)
    phone_entry.grid(row=8, column=1, padx=10, pady=5)
    entries["Phone Number"] = phone_entry

    result = {}

    def submit():
        for key, entry in entries.items():
            result[key] = entry.get()
        form.destroy()

    tk.Button(form, text="Submit", command=submit).grid(
        row=9, column=0, columnspan=2, pady=10)
    form.wait_window()
    return result


def create_airline_form(root):
    form = tk.Toplevel(root)
    form.title("Create Airline Record")
    form.grab_set()
    entries = {}

    tk.Label(form, text="Company Name").grid(
        row=0, column=0, padx=10, pady=5, sticky="e")
    company_entry = tk.Entry(form, width=30)
    company_entry.grid(row=0, column=1, padx=10, pady=5)
    entries["Company Name"] = company_entry

    result = {}

    def submit():
        for key, entry in entries.items():
            result[key] = entry.get()
        form.destroy()

    tk.Button(form, text="Submit", command=submit).grid(
        row=1, column=0, columnspan=2, pady=10)
    form.wait_window()
    return result


def create_flight_form(root):
    form = tk.Toplevel(root)
    form.title("Create Flight Record")
    form.grab_set()
    entries = {}

    tk.Label(form, text="Client ID").grid(
        row=0, column=0, padx=10, pady=5, sticky="e")
    client_entry = tk.Entry(form, width=30)
    client_entry.grid(row=0, column=1, padx=10, pady=5)
    entries["Client ID"] = client_entry

    tk.Label(form, text="Airline ID").grid(
        row=1, column=0, padx=10, pady=5, sticky="e")
    airline_entry = tk.Entry(form, width=30)
    airline_entry.grid(row=1, column=1, padx=10, pady=5)
    entries["Airline ID"] = airline_entry

    tk.Label(form, text="Date (DD-MM-YYYY)").grid(row=2,
                                                  column=0, padx=10, pady=5, sticky="e")
    date_entry = tk.Entry(form, width=30)
    date_entry.grid(row=2, column=1, padx=10, pady=5)
    entries["Date (DD-MM-YYYY)"] = date_entry

    tk.Label(form, text="Start City").grid(
        row=3, column=0, padx=10, pady=5, sticky="e")
    start_entry = tk.Entry(form, width=30)
    start_entry.grid(row=3, column=1, padx=10, pady=5)
    entries["Start City"] = start_entry

    tk.Label(form, text="End City").grid(
        row=4, column=0, padx=10, pady=5, sticky="e")
    end_entry = tk.Entry(form, width=30)
    end_entry.grid(row=4, column=1, padx=10, pady=5)
    entries["End City"] = end_entry

    result = {}

    def submit():
        for key, entry in entries.items():
            result[key] = entry.get()
        form.destroy()

    tk.Button(form, text="Submit", command=submit).grid(
        row=5, column=0, columnspan=2, pady=10)
    form.wait_window()
    return result
