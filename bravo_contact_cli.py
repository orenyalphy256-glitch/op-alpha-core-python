""" bravo_contact_cli.py - A simple command-line contact manager with remote lookup capability."""
# bravo_contact_cli.py

# Import necessary libraries
import csv
import requests

# Name of the CSV file to store contacts
CSVFILE = "contacts_bravo.csv"

# Function to add a contact
def add_contact(name, phone):
    with open(CSVFILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone])

# Function to list all contacts
def list_contacts():
    try:
        with open(CSVFILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader, start=1):
                print(i, "-", row[0], row[1])
    except FileNotFoundError:
        print("No contacts yet.")

# Function to lookup a contact remotely
def lookup_remote(name):
    params = {"q": name}
    r = requests.get("https://httpbin.org/get", params=params, timeout=5)
    print("Remote lookup status:", r.status_code)

# Main command loop
def main():
    while True:
        cmd = input("Enter command (add, list, lookup, quit): ").strip().lower()
        if cmd == "add":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            add_contact(name, phone)
            print("Added.")
        elif cmd == "list":
            list_contacts()
        elif cmd == "lookup":
            name = input("Name to lookup: ").strip()
            lookup_remote(name)
        elif cmd == "quit":
            break
        else:
            print("Unknown command")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

