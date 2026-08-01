"""
Contact Book
------------
A tiny command-line contact manager built to practice:
  - Lists   -> storing all contacts, append/remove/sort
  - Dicts   -> each contact is a {name, phone, city} record
  - Tuples  -> each contact also gets an immutable (id, created_order) tag
  - Sets    -> used to instantly check for duplicate phone numbers

Run it with:  python3 main.py
"""

contacts = []          # List of dicts -> holds all contact records
phone_numbers = set()  # Set -> tracks phone numbers already used (no duplicates allowed)
next_id = 1             # simple counter used to build each contact's tuple id


def add_contact(name, phone, city):
    global next_id

    # SET: reject duplicate phone numbers in O(1) time
    if phone in phone_numbers:
        print(f"⚠️  A contact with phone {phone} already exists. Not added.")
        return

    # TUPLE: immutable metadata that should never change once created
    meta = (next_id, "created")

    # DICT: the actual contact record
    contact = {
        "id_meta": meta,
        "name": name,
        "phone": phone,
        "city": city,
    }

    # LIST: append the new contact to our master list
    contacts.append(contact)
    phone_numbers.add(phone)
    next_id += 1
    print(f"✅ Added {name} (ID {meta[0]})")


def remove_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)          # list.remove()
            phone_numbers.discard(contact["phone"])  # set.discard() -> safe, no KeyError
            print(f"🗑️  Removed {name}")
            return
    print(f"❌ No contact named '{name}' found.")


def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def sort_contacts_by_name():
    contacts.sort(key=lambda c: c["name"].lower())  # list.sort()
    print("📇 Contacts sorted alphabetically by name.")


def list_contacts():
    if not contacts:
        print("📭 No contacts saved yet.")
        return
    print("\n--- Contact Book ---")
    for c in contacts:
        cid, _ = c["id_meta"]
        print(f"[{cid}] {c['name']} | 📞 {c['phone']} | 🏙️  {c['city']}")
    print(f"Total unique phone numbers on file: {len(phone_numbers)}\n")  # len(set)


def show_menu():
    print("""
1. Add contact
2. Remove contact
3. Search contact
4. Sort contacts by name
5. List all contacts
6. Exit
""")


def main():
    # seed a couple of sample contacts so the app isn't empty on first run
    add_contact("Aishwarya Mate", "9876543210", "Mumbai")
    add_contact("Rahul Sharma", "9123456780", "Pune")

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            city = input("City: ").strip()
            add_contact(name, phone, city)

        elif choice == "2":
            name = input("Name to remove: ").strip()
            remove_contact(name)

        elif choice == "3":
            name = input("Name to search: ").strip()
            result = search_contact(name)
            print(result if result else f"❌ No contact named '{name}' found.")

        elif choice == "4":
            sort_contacts_by_name()

        elif choice == "5":
            list_contacts()

        elif choice == "6":
            print("👋 Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
