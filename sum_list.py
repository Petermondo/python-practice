sum_list.py

# calculate the sum of numbers in a list
def mysum(numbers):
    sum = 0
    for number in numbers:  
        sum += number       
    return sum

# Test the function
myList = [1, 7, 10, 20, 11, 23, 47]
print("Sum =", mysum(myList))
