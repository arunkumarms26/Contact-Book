import json


# =========================
# CONTACT CLASS
# =========================

class Contact:

    def __init__(self, contact_id, name, phone, email):
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

    def display_contact(self):
        print("Contact ID :", self.id)
        print("Name       :", self.name)
        print("Phone      :", self.phone)
        print("Email      :", self.email)
        print("_" * 30)
        print()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }


# =========================
# CONTACT MANAGER CLASS
# =========================

class ContactManager:

    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []

        self.load_contacts()

    # Load contacts from JSON
    def load_contacts(self):

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            self.contacts = [
                Contact(
                    contact["id"],
                    contact["name"],
                    contact["phone"],
                    contact["email"]
                )
                for contact in data
            ]

        except FileNotFoundError:
            self.contacts = []

        except json.JSONDecodeError:
            print("Invalid JSON file.")
            self.contacts = []

    # Save contacts to JSON
    def save_contacts(self):

        data = [
            contact.to_dict()
            for contact in self.contacts
        ]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Add contact
    def add_contact(self, contact):

        for existing_contact in self.contacts:

            if existing_contact.id == contact.id:
                return False

        self.contacts.append(contact)
        self.save_contacts()

        return True

    # Show all contacts
    def show_contacts(self):

        if not self.contacts:
            print("No contacts available.")
            return

        for contact in self.contacts:
            contact.display_contact()

    # Search contact
    def search_contact(self, contact_id):

        for contact in self.contacts:

            if contact.id == contact_id:
                return contact

        return None

    # Update contact
    def update_contact(
        self,
        contact_id,
        name,
        phone,
        email
    ):

        contact = self.search_contact(contact_id)

        if contact is None:
            return False

        contact.name = name
        contact.phone = phone
        contact.email = email

        self.save_contacts()

        return True

    # Delete contact
    def delete_contact(self, contact_id):

        contact = self.search_contact(contact_id)

        if contact is None:
            return False

        self.contacts.remove(contact)

        self.save_contacts()

        return True


# =========================
# INPUT VALIDATION
# =========================

def get_contact_id():

    while True:

        try:
            contact_id = int(
                input("Enter Contact ID: ")
            )

            if contact_id <= 0:
                print("Contact ID must be greater than 0.")
                continue

            return contact_id

        except ValueError:
            print("Please enter a valid number.")


def get_phone():

    while True:

        phone = input(
            "Enter Phone: "
        ).strip()

        if not phone.isdigit():
            print("Phone number must contain only digits.")
            continue

        if len(phone) != 10:
            print("Phone number must be exactly 10 digits.")
            continue

        return phone


def get_email():

    while True:

        email = input(
            "Enter Email: "
        ).strip()

        if "@" not in email or "." not in email:
            print("Please enter a valid email.")
            continue

        return email


def get_name():

    while True:

        name = input(
            "Enter Name: "
        ).strip()

        if not name:
            print("Name cannot be empty.")
            continue

        return name


# =========================
# MAIN FUNCTION
# =========================

def main():

    manager = ContactManager()

    while True:

        print("\n=== CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input(
            "Enter your choice: "
        )

        # -------------------------
        # ADD CONTACT
        # -------------------------

        if choice == "1":

            contact_id = get_contact_id()

            if manager.search_contact(contact_id):
                print("Contact ID already exists!")
                continue

            name = get_name()

            phone = get_phone()

            email = get_email()

            contact = Contact(
                contact_id,
                name,
                phone,
                email
            )

            success = manager.add_contact(contact)

            if success:
                print("Contact added successfully!")
            else:
                print("Contact ID already exists!")

        # -------------------------
        # SHOW CONTACTS
        # -------------------------

        elif choice == "2":

            manager.show_contacts()

        # -------------------------
        # SEARCH CONTACT
        # -------------------------

        elif choice == "3":

            contact_id = get_contact_id()

            contact = manager.search_contact(
                contact_id
            )

            if contact:

                print("\nContact found:")
                contact.display_contact()

            else:

                print("Contact not found.")

        # -------------------------
        # UPDATE CONTACT
        # -------------------------

        elif choice == "4":

            contact_id = get_contact_id()

            contact = manager.search_contact(
                contact_id
            )

            if not contact:

                print("Contact not found.")
                continue

            print("\nEnter new details:")

            name = get_name()

            phone = get_phone()

            email = get_email()

            success = manager.update_contact(
                contact_id,
                name,
                phone,
                email
            )

            if success:
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        # -------------------------
        # DELETE CONTACT
        # -------------------------

        elif choice == "5":

            contact_id = get_contact_id()

            contact = manager.search_contact(
                contact_id
            )

            if not contact:

                print("Contact not found.")
                continue

            success = manager.delete_contact(
                contact_id
            )

            if success:
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        # -------------------------
        # EXIT
        # -------------------------

        elif choice == "6":

            print("Thank you for using Contact Book!")
            break

        else:

            print("Invalid choice. Please try again.")


# =========================
# PROGRAM START
# =========================

if __name__ == "__main__":
    main()