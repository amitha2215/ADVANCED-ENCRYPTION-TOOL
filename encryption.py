from cryptography.fernet import Fernet
import os

# Function to generate a secret key (Run only once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔑 Secret key generated and saved as 'secret.key'.")

# Function to load the existing secret key
def load_key():
    if not os.path.exists("secret.key"):
        print("❌ Error: 'secret.key' not found! Run generate_key() first.")
        return None
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_path):
    key = load_key()
    if key is None:
        return

    cipher = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        encrypted_data = cipher.encrypt(file_data)

        with open(file_path + ".enc", "wb") as file:
            file.write(encrypted_data)

        print(f"✅ File '{file_path}' encrypted successfully! Saved as '{file_path}.enc'.")

    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")

# Function to decrypt a file
def decrypt_file(file_path):
    key = load_key()
    if key is None:
        return

    cipher = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        original_file_path = file_path.replace(".enc", "")
        with open(original_file_path, "wb") as file:
            file.write(decrypted_data)

        print(f"✅ File '{file_path}' decrypted successfully! Restored as '{original_file_path}'.")

    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
    except Exception:
        print("❌ Error: Decryption failed. Incorrect key or corrupted file.")
