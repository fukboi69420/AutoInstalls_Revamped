import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Generate a secure key
def generate_key(password):
    salt = b'\x9d\x8b\x8f\x8b\x9d\x8b\x8f\x8b'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

# Encrypt a file
def encrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name, 'wb') as file:
        file.write(decrypted_data)

# Main function
def main():
    password = input("Enter encryption password: ").encode()
    key = generate_key(password)
    file_name = input("Enter file name: ")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")
    if choice == 'E':
        encrypt_file(file_name, key)
    elif choice == 'D':
        decrypt_file(file_name, key)

if __name__ == "__main__":
    main()
