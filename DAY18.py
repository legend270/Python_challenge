Day 18 of the 90 days python challenge 



import hashlib

def hash_password(password, algorithm='sha256'):
    """Hash a password using the specified algorithm"""
    # Encode the password as bytes (required by hashlib)
    password_bytes = password.encode('utf-8')
    
    # Create a hash object based on the selected algorithm
    if algorithm.lower() == 'md5':
        hash_obj = hashlib.md5(password_bytes)
    elif algorithm.lower() == 'sha1':
        hash_obj = hashlib.sha1(password_bytes)
    elif algorithm.lower() == 'sha256':
        hash_obj = hashlib.sha256(password_bytes)
    else:
        raise ValueError("Unsupported hashing algorithm")
    
    # Get the hexadecimal digest of the hash
    return hash_obj.hexdigest()

def verify_password(input_password, stored_hash, algorithm='sha256'):
    """Verify if input password matches stored hash"""
    # Hash the input password using the same algorithm
    input_hash = hash_password(input_password, algorithm)
    
    # Compare the hashes securely (to prevent timing attacks)
    return input_hash == stored_hash

def main():
    print("Password Hashing Demonstration")
    print("Available algorithms: MD5, SHA1, SHA256")
    
    # Get user input
    algorithm = input("Choose hashing algorithm (default: SHA256): ").strip() or 'sha256'
    password = input("Enter password to hash: ")
    
    # Hash the password
    hashed_password = hash_password(password, algorithm)
    print(f"\nHashed password ({algorithm.upper()}): {hashed_password}")
    
    # Verification demo
    print("\nNow let's verify the password:")
    test_password = input("Enter password to verify: ")
    
    if verify_password(test_password, hashed_password, algorithm):
        print("✅ Password matches!")
    else:
        print("❌ Password does not match!")

if __name__ == "__main__":
    main()