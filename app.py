import streamlit as st
from main import Contact, ContactManager


st.set_page_config(
    page_title="Contact Book",
    page_icon="📱",
    layout="wide"
)


manager = ContactManager()


st.title("📱 Contact Book")
st.write("Manage your contacts using Streamlit.")


option = st.sidebar.selectbox(
    "Select Operation",
    [
        "Add Contact",
        "Show Contacts",
        "Search Contact",
        "Update Contact",
        "Delete Contact"
    ]
)


# =========================
# ADD CONTACT
# =========================

if option == "Add Contact":

    st.header("➕ Add Contact")

    contact_id = st.number_input(
        "Contact ID",
        min_value=1,
        step=1
    )

    name = st.text_input("Name")

    phone = st.text_input("Phone")

    email = st.text_input("Email")

    if st.button("Add Contact"):

        if not name.strip():

            st.error("Name cannot be empty.")

        elif not phone.isdigit():

            st.error("Phone number must contain only digits.")

        elif len(phone) != 10:

            st.error("Phone number must be exactly 10 digits.")

        elif "@" not in email or "." not in email:

            st.error("Please enter a valid email.")

        elif manager.search_contact(int(contact_id)):

            st.error("Contact ID already exists.")

        else:

            contact = Contact(
                int(contact_id),
                name.strip(),
                phone,
                email.strip()
            )

            success = manager.add_contact(contact)

            if success:
                st.success("Contact added successfully!")


# =========================
# SHOW CONTACTS
# =========================

elif option == "Show Contacts":

    st.header("📋 All Contacts")

    contacts = manager.contacts

    if not contacts:

        st.info("No contacts available.")

    else:

        data = []

        for contact in contacts:

            data.append({
                "Contact ID": contact.id,
                "Name": contact.name,
                "Phone": contact.phone,
                "Email": contact.email
            })

        st.dataframe(
            data,
            width="stretch"
        )


# =========================
# SEARCH CONTACT
# =========================

elif option == "Search Contact":

    st.header("🔍 Search Contact")

    contact_id = st.number_input(
        "Enter Contact ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        contact = manager.search_contact(
            int(contact_id)
        )

        if contact:

            st.success("Contact found!")

            st.write("**Contact ID:**", contact.id)
            st.write("**Name:**", contact.name)
            st.write("**Phone:**", contact.phone)
            st.write("**Email:**", contact.email)

        else:

            st.error("Contact not found.")


# =========================
# UPDATE CONTACT
# =========================

elif option == "Update Contact":

    st.header("✏️ Update Contact")

    contacts = manager.contacts

    if not contacts:

        st.info("No contacts available.")

    else:

        contact_ids = [
            contact.id
            for contact in contacts
        ]

        selected_id = st.selectbox(
            "Select Contact ID",
            contact_ids
        )

        contact = manager.search_contact(
            selected_id
        )

        name = st.text_input(
            "Name",
            value=contact.name
        )

        phone = st.text_input(
            "Phone",
            value=contact.phone
        )

        email = st.text_input(
            "Email",
            value=contact.email
        )

        if st.button("Update Contact"):

            if not name.strip():

                st.error("Name cannot be empty.")

            elif not phone.isdigit():

                st.error(
                    "Phone number must contain only digits."
                )

            elif len(phone) != 10:

                st.error(
                    "Phone number must be exactly 10 digits."
                )

            elif "@" not in email or "." not in email:

                st.error("Please enter a valid email.")

            else:

                success = manager.update_contact(
                    selected_id,
                    name.strip(),
                    phone,
                    email.strip()
                )

                if success:
                    st.success(
                        "Contact updated successfully!"
                    )


# =========================
# DELETE CONTACT
# =========================

elif option == "Delete Contact":

    st.header("🗑️ Delete Contact")

    contacts = manager.contacts

    if not contacts:

        st.info("No contacts available.")

    else:

        contact_ids = [
            contact.id
            for contact in contacts
        ]

        selected_id = st.selectbox(
            "Select Contact ID",
            contact_ids
        )

        contact = manager.search_contact(
            selected_id
        )

        st.write("**Name:**", contact.name)
        st.write("**Phone:**", contact.phone)
        st.write("**Email:**", contact.email)

        if st.button("Delete Contact"):

            success = manager.delete_contact(
                selected_id
            )

            if success:
                st.success(
                    "Contact deleted successfully!"
                )