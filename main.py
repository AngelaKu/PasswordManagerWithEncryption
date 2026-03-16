# -------------------------
# 1. Imports
# -------------------------
import hashlib
import os
from password_manager import add_new_password, view_passwords
from crypto_utils import load_key


# -------------------------
# 2. Master password system
# -------------------------
MASTER_FILE = "master.hash"

def set_master_password():
    pwd = input("Set a master password: ")
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    with open(MASTER_FILE, "w") as f:
        f.write(hashed)
    print("Master password set.")

def verify_master_password():
    if not os.path.exists(MASTER_FILE):
        print("No master password found. Creating one now.")
        set_master_password()

    pwd = input("Enter master password: ")
    hashed = hashlib.sha256(pwd.encode()).hexdigest()

    with open(MASTER_FILE, "r") as f:
        stored = f.read().strip()

    if hashed == stored:
        print("Access granted.")
        return True
    else:
        print("Access denied.")
        return False


# -------------------------
# 3. Menu system (Step 5)
# -------------------------
def main_menu():
    while True:
        print("\n=== Password Manager ===")
        print("1. Add new password")
        print("2. View passwords")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_new_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


# -------------------------
# 4. Program entry point
# -------------------------
if __name__ == "__main__":
    load_key()  # ensures encryption key exists

    if verify_master_password():
        main_menu()