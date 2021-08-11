"""
# What will this do?
for i in range(5):
    print(i)
"""



"""
# What will this do?
for i in range(1, 10, 2):
    print(i)
"""



"""
# What will this do?
for i in range(10, 2, -2):
    print(i)
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Tsepo', 'Jade', 'Thavha']
for name in list_of_names:
    print(name)
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Tsepo', 'Jade', 'Thavha']
for name in range(len(list_of_names)):
    print(name)
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Tsepo', 'Jade', 'Thavha']
for name in range(len(list_of_names), 10, 1):
    print(name)
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Tsepo', 'Jade', 'Thavha']
for name in range(len(list_of_names)):
    print(list_of_names[name])
"""




"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Tsepo', 'Jade', 'Thavha', 'Jason']
for name in range(len(list_of_names[0:3])):
    print(name)
"""




"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Tsepo', 'Jade', 'Thavha']
for name in list_of_names:
    for character in name:
        print(character)
"""




"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando']
for name in list_of_names:
    for character in name:
        print(name)
"""




"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando']
for name in list_of_names:
    for character in name:
        print(character)
        if character == 'p':
            break
"""




"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Eckard']
for name in list_of_names:
    for character in name:
        print(character)
        if character == 'p':
            break
        break
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Eckard']
for name in list_of_names:
    for character in name:
        print(character)
        if character == 'p':
            break
    break
#"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando']
for name in list_of_names:
    for character in name:
        print(character)
        if character in 'pn':
            break
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando']
for name in list_of_names:
    print(name)
print("Finished")
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Eckard']
for name in list_of_names:
    for char in name:
        print(char)
    print('Nested loop finished.')
print('Outside loop finished.')
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Mahlori']
for name in list_of_names:
    for char in name:
        print(char)
        continue
    print('Outside loop finished.')
    continue
"""



"""
# What will this code do?
list_of_names = ['Thapelo', 'Mahlori']
for name in list_of_names:
    if 'o' in name:
        for char in name:
            continue
        print("Hello")
        break
print('Outside loop finished.')
"""



"""
list_of_names = ['Thapelo', 'Mahlori', 'Eckard']
for name in list_of_names:
    for char in name:
        if 'o' in name:
            for char in name:
                continue
            print("Hello")
            break
print('Outside loop finished.')
"""




"""
# What do we need to do to print the main diagonal of 7, 5, 3?
my_list = [9, 5, 1]
#[0][0] = 7
#[1][1] = 5
#[2][2] = 3

#  9
# 5
#1
"""






"""
list_of_numbers = [3, 5, 7]
for index in range(2,-1,-1):
    print(" " * (len(list_of_numbers) - 1 - index) + str(list_of_numbers[index]))
"""



"""
# What do we need to do to print the main diagonal of 7, 5, 3?
list_of_numbers = [9, 5, 1]
len = len(list_of_numbers)
for idx_one in range(3):
    print((len - idx_one)*' ' + str(list_of_numbers[idx_one]))

#print([0][2])
#print([1][1])
#print([2][0])

#  9
# 5
#1
"""




"""
# What will this code do?
def a_yield_function():
    list_of_names = ['Thapelo', 'Thando', 'Eckard']
    for name in list_of_names:
        yield name

x = a_yield_function()
print(f'x = {x}')
"""



"""
# What will this code do?
def a_yield_function():
    list_of_names = ['Thapelo', 'Thando', 'Eckard']
    for name in list_of_names:
        yield name

for x in a_yield_function():
    print(x)
"""



"""
# What will this code do?
def a_yield_function():
    range_of_integers = range(1, 20, 2)
    for number in range_of_integers:
        yield number*number

x = list(a_yield_function())
"""



"""
*
**
***
****
*****
# One if statement
# Two for loops
# triangle(-5)
*****
 ****
  ***
   **
    *
"""
