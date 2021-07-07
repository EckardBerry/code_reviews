"""
"What will this do?"
def something():
    print("Hello")
    return None

x = something()
print(f'x = {x}')
"""



"""
"What will this do?"
def something():
    print("Hello")

x = something()
print(f'x = {x}')
"""



"""
"What will this do?"
def something():
    print("Hello")
    return None
    return "blue"

x = something()
print(f'x = {x}')
"""


"""
"What will this do?"
def something():
    print("Hello")
    return None
    return "blue"

x = something()
print(f'x = {x}')
print(f'x = {x}')
"""



"""
"What will this do?"
def something(parameter):
    print("Hello")
    return parameter

x = something("Your Name")
print(f'x = {x}')
"""


"""
"What will this do?"
def something(parameter):
    print("Hello")
    return parameter

x = something("Your Name")
x = something("Hopeful")
print(f'x = {x}')
"""


"""
"What will this do?"
def something(parameter):
    print("Hello")
    return parameter

x = something("Your Name")
print(f'x = {x}')
x = something("Hopeful")
print(f'x = {x}')
"""


"""
"What will this do?"
def something(parameter):
    print("Hello")
    if parameter == "Your Name":
        return parameter
    return "Whats your name?"

x = something("Your Name")
print(f'x = {x}')
x = something("Hopeful")
print(f'x = {x}')
"""


"""
"What will this do?"
def something(parameter):
    print("Hello")
    for x in parameter:
        print(x)

x = something("Your Name")
print(f'x = {x}')
"""


"""
"What will this do?"
def something(parameter):
    print("Hello")
    for x in parameter:
        print(x)
        return x
    return parameter

x = something("Your Name")
print(f'x = {x}')
"""


"""
def first_func(param_1):
    return param_1

def second_func(param_2):
    if param_2 == "Hello":
        return first_func(param_2)
    return second_func(param_2)

def third_func(param_3):
    second_func(param_3)
    if second_func(param_3):
        return param_3, "Simple"
    return 'Nothing'

x = second_func('Goodbye')
print(f'x = {x}')
x = third_func('Get this')
print(f'x = {x}')
"""



"""
def first_func(param_1):
    return param_1 + " Sugar"

def second_func(param_2):
    if param_2 == "Hello":
        return first_func(param_2)
    return second_func(param_2)

def third_func(param_3):
    second_func(param_3)
    if second_func(param_3):
        return param_3, "Simple"
    return 'Nothing'

x = second_func('Hello')
print(f'x = {x}')
x = third_func('Hello')
print(f'x = {x}')
"""



"""
def first_func(param_1):
    return param_1 + " Sugar"

def second_func(param_2):
    if param_2 == "Hello":
        return first_func(param_2)
    return second_func(param_2)

def third_func(param_3):
    second_func(param_3)
    if param_3 == 'Goodbye':
        return param_3, "Simple"
    return 'Nothing'

x = second_func('Hello')
print(f'x = {x}')
x = third_func('Hello')
print(f'x = {x}')
"""

