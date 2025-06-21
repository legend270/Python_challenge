#Day 10 of the 90 days python challenge
import math

def calculate_square_root():
    """
    Calculates the square root of a number provided by the user.
    Handles invalid input gracefully.
    """
    print("Square Root Calculator")
    print("----------------------")
    
    while True:
        # Get user input
        user_input = input("Enter a number (or 'q' to quit): ")
        
        # Check for quit command
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        try:
            # Convert to float
            number = float(user_input)
            
            # Check for negative numbers
            if number < 0:
                print("Error: Cannot calculate square root of a negative number.")
                continue
            
            # Calculate square root
            result = math.sqrt(number)
            
            # Display result with 4 decimal places
            print(f"The square root of {number} is {result:.4f}")
            
        except ValueError:
            print("Error: Please enter a valid number.")

# Run the calculator
if __name__ == "__main__":
    calculate_square_root()