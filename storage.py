from crypto_utils import get_fernet

DATA_FILE = "vault.dat"

def add_entry(site, username, password):
    f = get_fernet()
    line = f"{site}|{username}|{password}"
    token = f.encrypt(line.encode())

    with open(DATA_FILE, "ab") as file:
        file.write(token + b"\n")

def read_entries():
    entries = []
    f = get_fernet()

    try:
        with open(DATA_FILE, "rb") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                decrypted = f.decrypt(line).decode()
                site, username, password = decrypted.split("|")
                entries.append((site, username, password))
    except FileNotFoundError:
        pass

    return entries