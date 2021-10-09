"""
# What will this do?
for i in 'pink':
    print(i)
"""

def foo():
    print('Hello')

x = foo()
print(f'x = {x}')



"""
# What will this do?
names = ['a', 'b', 'c']
for index in range(len(names)):
    print(index)
"""




"""
# What will this do?
names = ['a', 'b', 'c']
for j in range(len(names)):
    print(names[j])
"""




"""
# What will this do?
names = ['a', 'b', 'c']
for index in range(len(names)):
    print(index)
    print(names[index])
"""




"""
# What will this do?
names = ['a', 'b', 'c']
for index in range(len(names)):
    print(index)
    if names[index] == 'b':
        print(index)
    else:
        print(names[index])
"""



"""
# What will this do?
for i in range(1, 5, 1):
    print(i)
"""



"""
# What will this do?
for i in range(10, 2, -2):
    print(i)
    if i == 4:
        for j in range(5):
            continue
        break
    break
"""




"""
# What will this code do?
list_of_names = ['Thapelo', 'Thando', 'Tsepo', 'Jade', 'Thavha']
for name in list_of_names:
    print(name)
    if name == 'Tsepo':
        for char in name:
            print(char)
            break
    print(name)
    break
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
list_of_names = ['Thapelo', 'Thando', 'Hero', 'Zero']
for i in range(len(list_of_names)):
    if i == 1:
        print(list_of_names[i])
    else:
        continue
    
    for j in range(len(list_of_names[i])):
        print(list_of_names[i-1])
"""




"""
# What will this do?
for k in range(10, 5, -1):
    if k == 8:
        print(k+1)
    else:
        for i in range(4):
            if i == 2:
                print(i+1)
            else:
                continue
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
"""




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
    break
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
While Loops
"""


"""
i = 5
while i != 10:
    if i == 8:
        i+=1
        continue
    else:
        print(i)
    i+=1
"""



"""
# What will this do
i = 4
while i > 0:
    print(i)
    if i == 2:
        while i > 1:
            print(i)
            i -= 1
    else:
        print(i)
        i -= 1
        continue
"""




"""
# What will this do
i = 10
while i > 0:
    print(i)
    if i == 5:
        break
    else:
        print(i-1)
        i -= 1
        continue
"""



"""
# What will this do
i = 5
while i > 0:
    print(i)
    if i == 2:
        continue
    else:
        break
    i -= 1
"""



"""
# What will this do
i = 3
while i > 0:
    j = i-1
    while j > 0 and j != i:
        print(i)
        if i == 2:
            break
        i -= 1
    i -= 1
"""



"""
# What will this do
i = 3
while i > 0:
    j = i-1
    while j > 0 and j != i:
        print(i)
        if i == j:
            continue
        i -= 1
    i -= 1
"""




"""
# What will this do
LIST = ['John', 'Jacob', 'sitting']
i = len(LIST)
while i != 0:
    j = i - 1
    while j >= 0 and j < i:
        print(LIST[j])
        j += 1
    i -= 1
"""



"""
# What will this do
LIST = ['John', 'Jacob', 'sitting']
i = len(LIST)
while i != 0:
    print(i)
    j = len(LIST) - i
    if j == i+1:
        continue
    break
"""



"""
# What will this do?
mine = ['Dlamini', 'Mashau', 'Baloyi', 'Berry']
i = len(mine) - len(mine)

while mine[i] in mine:
    if i > len(mine):
        break
    else:
        print(mine[i])
        i += 1
        if i == len(mine):
            i += 1
            while i < 8:
                print(mine[2])
                continue
        else:
            break
"""



