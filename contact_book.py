"""contact_book.py - Simple contact book application."""

# contact_book.py

FILENAME = "contacts.txt"

def add_contact(name, phone):
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"{name},{phone}\n")

def list_contacts():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                name, phone = line.strip().split(",", 1)
                print(name, phone)
    except FileNotFoundError:
        print("No contacts yet.")

if __name__ == "__main__":
    # quick demo
    add_contact("TestUser", "0712345678")
    list_contacts()
