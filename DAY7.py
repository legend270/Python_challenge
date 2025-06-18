def user_info_system():
    # Dictionary to store multiple users
    users = {}
    
    while True:
        print("\nUser Information System")
        print("1. Add User")
        print("2. Retrieve User")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            # Add a new user
            name = input("Enter user's name: ")
            age = input("Enter user's age: ")
            email = input("Enter user's email: ")
            
            users[name] = {
                "age": age,
                "email": email
            }
            print(f"User {name} added successfully!")
            
        elif choice == "2":
            # Retrieve user information
            name = input("Enter the name of the user to retrieve: ")
            
            if name in users:
                user_data = users[name]
                print(f"\nUser Information for {name}:")
                print(f"Age: {user_data['age']}")
                print(f"Email: {user_data['email']}")
            else:
                print(f"No user found with name: {name}")
                
        elif choice == "3":
            print("Exiting the program...")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
user_info_system()