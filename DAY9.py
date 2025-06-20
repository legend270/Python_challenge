def get_valid_number():
    while True:
        try:
            num = int(input("Please enter an integer: "))
            return num  # Exit the loop if input is valid
        except ValueError:
            print("That's not a valid integer. Please try again.")
        finally:
            print("Attempt completed.")  # This runs every loop

def main():
    print("Welcome to the Number Validator!")
    number = get_valid_number()
    print(f"You entered a valid number: {number}")

if __name__ == "__main__":
    main()