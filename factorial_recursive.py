# factorial_recursive.py

# Function to calculate factorial using recursion
def rf(x):
    if x == 0 or x == 1:  # Base case
        return 1
    else:
        return x * rf(x - 1)  # Recursive call

# Test the recursive function
print(rf(5))
