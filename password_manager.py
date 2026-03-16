from storage import add_entry, read_entries

def add_new_password():
    site = input("Site/App: ")
    username = input("Username: ")
    password = input("Password: ")
    add_entry(site, username, password)
    print("Entry added.")

def view_passwords():
    entries = read_entries()
    if not entries:
        print("No entries found.")
        return

    for i, (site, username, password) in enumerate(entries, start=1):
        print(f"{i}. Site: {site}, Username: {username}, Password: {password}")