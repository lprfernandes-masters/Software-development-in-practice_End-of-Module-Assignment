# RoamWide Travel Record Management System

This project was developed to build a record management system for a specialized travel agency. The system can handle three different types of records:

Client Records
Flight Records
Airline Records

The system provides a simple and intuitive Graphical User Interface (GUI) that allows users to:

Create, Delete, Update, and Search/Display records
Store and manage records using Python's list of dictionaries
Save records to the file system in JSON and load them upon starting the application

# Features

Create a Record: Add new client, flight, or airline records.
Delete a Record: Remove an existing record.
Update a Record: Edit details of an existing record.
Search and Display a Record: Search for records and view detailed information.

# The records are stored as follows:

# Client Record Format
- **ID**: int
- **Type**: Client
- **Name**: string
- **Address Line 1**: string
- **Address Line 2**: string
- **Address Line 3**: string
- **City**: string
- **State**: string
- **Zip Code**: string
- **Country**: string
- **Phone Number**: string

# Airline Record Format
- **ID**: int
- **Type**: string (type of record)
- **Company Name**: string

# Flight Record Format
- **Client_ID**: int
- **Airline_ID**: int
- **Date**: date/time
- **Start City**: string
- **End City**: string

# Technologies Used
- Python for backend programming
- Tkinter for GUI
- JSON for data persistence

# Prerequisites
- Python 3.12.4 installed