# sum_digits.py

# Function to calculate the sum of digits of a given number
def sd(n):
    total = 0
    while n > 0:
        total += n % 10  # Add the last digit to total
        n //= 10         # Remove the last digit
    return total

# Test the function
print(sd(12345))
