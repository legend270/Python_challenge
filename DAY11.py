#Day 11 of the 90 days python challenge


import re

def validate_email(email):
    """
    Validates an email address using regular expressions.
    Returns True if valid, False otherwise.
    """
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

def email_validator_app():
    """
    Interactive email validator application.
    """
    print("Email Address Validator")
    print("-----------------------")
    print("Enter email addresses to validate (type 'quit' to exit).\n")
    
    while True:
        email = input("Enter an email address: ").strip()
        
        if email.lower() == 'quit':
            print("Goodbye!")
            break
        
        if validate_email(email):
            print(f"✅ '{email}' is a valid email address.\n")
        else:
            print(f"❌ '{email}' is NOT a valid email address.\n")

if __name__ == "__main__":
    email_validator_app()