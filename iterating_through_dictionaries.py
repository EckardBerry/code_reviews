dictionary = {'Hello': 2, "Goodbye": 3, "Friend": 4, "Sing": "Bring", "Watch": "Time"}

#"""
# What will this do?
print(dictionary.values())
print(dictionary.items())
print(dictionary.keys())
#"""


"""
# What will this do?
print(dictionary.get("Goodbye"))
dictionary.pop("Sing")
print(dictionary)
"""


"""
# What will this do?
for i in dictionary:
    print(i)
"""




"""
# What will this do?
for i in dictionary.keys():
    print(i)
"""



"""
# What will this do?
for i in dictionary.values():
    print(i)
"""



"""
# What will this do?
for i in dictionary.items():
    print(i)
"""



"""
# What will this do?
for index, key in enumerate(dictionary):
    if key == "Hello":
        del dictionary[key]
        break
print(dictionary)
"""


"""
# What will this do?
for index, key in enumerate(dictionary.items()):
    print(index)
    print(key[0])
    print(key[1])
"""



"""
# What will this do?
for key, value in enumerate(dictionary):
    print(value)
"""



"""
# What will this do?
values = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9]
print(dict.fromkeys(values))
print(len(values) - len(dict.fromkeys(values)))
"""



"""
# What will this do?
empty_dictionary = {}
values = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9]
for value in values:
    for element in range(int(value), int(value) + 2):
        empty_dictionary.setdefault(element, []).append(value)
print(empty_dictionary)
"""




"""
# What will this do?
for key, val in enumerate(dictionary):
    print(key)
    print(val)
"""