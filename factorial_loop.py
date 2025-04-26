# factorial_loop.py

# Function to calculate the factorial of a number using a loop
def factorial(n): #p=result
    p = 1
    for i in range(1, n + 1):  # Multiply numbers from 1 to n
        p *= i
    return p

# Test the function
print(factorial(5))
