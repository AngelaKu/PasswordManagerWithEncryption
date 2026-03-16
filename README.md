# Password Manager with Encryption

A simple Python password manager that protects stored login information using encrypted storage and a master password. The project demonstrates secure data handling, basic encryption, and clean program structure.

---

## What It Does

- Uses a **master password** to lock/unlock the vault  
- Encrypts all saved passwords using **Fernet (AES‑based)** encryption  
- Stores credentials in an encrypted file  
- Lets you **add** and **view** saved passwords  
- Keeps the code organized across multiple Python files  

---

## How It Works

- On first run, you create a master password.  
- The program hashes it with SHA‑256 and saves only the hash.  
- A secure encryption key is generated and used to encrypt/decrypt entries.  
- Credentials are stored in an encrypted `.dat` file.  
- You can view them only after entering the correct master password.

---

## How to Run It

1. Install Python 3.10+  
2. Install the required library:

   ```bash
   pip install cryptography
   ```

3. Run the program:

   ```bash
   python main.py
   ```

---

## Files in This Project

- `main.py` — program entry + master password system  
- `crypto_utils.py` — encryption key handling  
- `storage.py` — encrypted file read/write  
- `password_manager.py` — add/view password functions  
- `.gitignore` — keeps sensitive files out of GitHub  (So this only shows the base coding.)

---

## Security Notes

- The encryption key, master password hash, and vault file are **not** included in the repo.  
- This personal project is for demonstration and testing, not production use. So please do not use this exact code in anything seriously important.
