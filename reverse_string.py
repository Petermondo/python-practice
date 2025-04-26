# reverse_string.py

# Function to reverse a string without using [::-1] or built-in methods
def reverse(s):
    rs = ""
    for char in s:  # Loop through each character
        rs = char + rs  # Build reversed string
    return rs

# Test the function
print(reverse("hello world"))
