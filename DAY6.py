#Day 6 of the 90 days challenge

def calculate_sum_and_average(numbers):
    
    #Calculates the sum and average of a list of numbers.
   
    if not numbers:  # Handle empty list case
        return 0, 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Get input from user
input_str = input("Enter numbers separated by spaces: ")
number_list = [float(num) for num in input_str.split()]

# Calculate results
sum_result, avg_result = calculate_sum_and_average(number_list)

# Display output
print(f"\nNumbers entered: {number_list}")
print(f"Sum: {sum_result}")
print(f"Average: {avg_result:.2f}")