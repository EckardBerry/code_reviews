
"""
# What will this do
def function():
    print("Hello")
    return 'Hello'

x = function()
print(f'x = {x}')
"""




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
    return 'Blue'

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

x = something("Yellow")
print(f'x = {x}')
"""




"""
"What will this do?"
def something(parameter):
    print("Hello")
    return parameter

x = something("Pink")
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
# What will this do?
def foo():
    for i in range(3):
        print(i)
        if i == 1:
            return i
        else:
            print('Bye')
    return None

x = foo()
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
#x = third_func('Get this')
#print(f'x = {x}')
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
#x = third_func('Hello')
#print(f'x = {x}')
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



"""
# What will happen here?
def foo_1(param_1):
    return "param_1"

def foo_2(param_2):
    return foo_1("Phenyo")

def foo_3(param_3):
    print("Hello")
    if param_3 == "J":
        return foo_2(param_3)
    return

x = foo_3("J")
print(f'x = {x}')
"""



"""
def func_1(param_1):
    print("Goodbye")
    for char in param_1:
        print(char)
        if char in "Goodbye":
            return char
        return param_1
    return

def func_2(param_2):
    if param_2 == 'Tsepo':
        return func_1(param_2)
    return

x = func_2("Tsepo")
print(f'x = {x}')
"""














"""
def foo(param):
    if first(param):
        return 'Your welcome'
    return


def first(param):
    for element in param:
        print(element)
    else:
        for element in param:
            if element in 'asdf':
                return foo('a')
            return foo


x = foo('asdf')
print(f'x = {x}')
x = first('asdf')
print(f'x = {x}')
"""


"""
def h_one(param):
    return True if 'x' in param else False
    
x = h_one
x = h_one('xyz')
print(f'x = {x("")}')
"""


"""
def prin(param):
    for p in param:
        return p
    return


def h_two(param):
    for p in param:
        return prin(p)

x = h_two('asdf')
print(f'x = {x}')
"""


"""
def prin(param):
    x = h_three('param')
    print(f'x = {x}')
    return


def h_three(param):
    if 'a' in param:
        return prin(param)
    return


x = h_three('asdf')
print(f'x = {x}')
"""

