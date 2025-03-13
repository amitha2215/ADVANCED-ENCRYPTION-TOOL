from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Decrypt a file
def decrypt_file(encrypted_file_path):
    key = load_key()
    cipher = Fernet(key)

    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    original_file_path = encrypted_file_path.replace(".enc", "")

    with open(original_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File '{encrypted_file_path}' decrypted successfully!")

if __name__ == "__main__":
    file_to_decrypt = input("Enter the file path to decrypt: ")
    decrypt_file(file_to_decrypt)
