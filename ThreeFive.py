# Have the function ThreeFiveMultiples(num) return the sum of all the multiples of 3 and 5 that are below num.
# For example: if num is 10, the multiples of 3 and 5 that are below 10 are 3, 5, 6, and 9, and adding them up you get
# 23, so your program should return 23. The integer being passed will be between 1 and 100.
# Use the Parameter Testing feature in the box below to test your code with different arguments.

def ThreeFiveMultiples(num):
    sum_of_multiples = 0
    for numbers in range(1, num):
        if numbers % 5 == 0 or numbers % 3 == 0:
            sum_of_multiples += numbers
    return sum_of_multiples

print(ThreeFiveMultiples(100))