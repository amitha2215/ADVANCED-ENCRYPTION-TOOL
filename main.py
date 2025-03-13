from encryption import generate_key, encrypt_file, decrypt_file
import os

def main():
    while True:
        print("\n🔐 Advanced Encryption Tool")
        print("1. Generate Secret Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            file_path = input("Enter the file path to encrypt: ")
            if os.path.exists(file_path):
                encrypt_file(file_path)
            else:
                print("❌ Error: File not found!")
        elif choice == "3":
            file_path = input("Enter the file path to decrypt: ")
            if os.path.exists(file_path):
                decrypt_file(file_path)
            else:
                print("❌ Error: File not found!")
        elif choice == "4":
            print("🔒 Exiting the Encryption Tool. Stay Safe!")
            break
        else:
            print("❌ Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
