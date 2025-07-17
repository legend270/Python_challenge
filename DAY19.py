pip install cryptography
from cryptography.fernet import Fernet

def generate_symmetric_key():
    """Generate a symmetric key for Fernet"""
    return Fernet.generate_key()

def symmetric_encrypt(message, key):
    """Encrypt a message using symmetric encryption"""
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def symmetric_decrypt(encrypted_message, key):
    """Decrypt a message using symmetric encryption"""
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
key = generate_symmetric_key()
message = "This is a secret message!"
encrypted = symmetric_encrypt(message, key)
decrypted = symmetric_decrypt(encrypted, key)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
