#Day 5 of the 90 days challenge


def factorial(n):
    """Calculate the factorial of a non-negative integer"""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test the function
print(factorial(5))  # Output: 120 (5! = 5×4×3×2×1 = 120)
print(factorial(0))  # Output: 1
print(factorial(-3)) # Output: Factorial is not defined for negative numbers