# from cryptography.fernet import Fernet

# # Function to generate a key for encryption
# def generate_key():
#     return Fernet.generate_key()

# # Function to encrypt data
# def encrypt_data(key, data):
#     cipher_suite = Fernet(key)
#     cipher_text = cipher_suite.encrypt(data.encode())
#     return cipher_text

# # Function to decrypt data
# def decrypt_data(key, cipher_text):
#     cipher_suite = Fernet(key)
#     plain_text = cipher_suite.decrypt(cipher_text).decode()
#     return plain_text

