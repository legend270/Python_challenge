#Day 12 of the 90 days python challenge 


import json

def json_file_reader():
    """Read a JSON file and display specific values based on user input."""
    
    # Get file path from user
    file_path = input("Enter the path to your JSON file: ")
    
    try:
        # Load the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            
        print("\nSuccessfully loaded JSON data!")
        
        while True:
            print("\nOptions:")
            print("1. View entire JSON structure")
            print("2. Search for a specific key")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                # Pretty print the entire JSON
                print("\nComplete JSON structure:")
                print(json.dumps(data, indent=4))
                
            elif choice == '2':
                # Search for a specific key
                key_path = input("Enter the key path (use dots for nested keys, e.g., 'user.address.city'): ")
                keys = key_path.split('.')
                
                current_data = data
                try:
                    for key in keys:
                        if isinstance(current_data, list):
                            key = int(key)  # Try to convert to index if it's a list
                        current_data = current_data[key]
                    
                    print(f"\nValue for '{key_path}':")
                    if isinstance(current_data, (dict, list)):
                        print(json.dumps(current_data, indent=4))
                    else:
                        print(current_data)
                        
                except (KeyError, IndexError, ValueError):
                    print(f"Key path '{key_path}' not found or invalid.")
                    
            elif choice == '3':
                print("Exiting...")
                break
                
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    json_file_reader()