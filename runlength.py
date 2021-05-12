# Have the function stringchallenge(str_arr) take the str_arr parameter being passed in
# and return a compressed verison of the string, for instance, aabbccddd should return
# 2aa2bb2cc3ddd
"""
import collections
def stringchallenge(str_arr):
    letters = collections.Counter(str_arr)
    empty_string = ''
    for key, value in letters.items():
        if value > 1:
            result = f'{value}{key}'
            empty_string += result
    return empty_string
"""

"""
def stringchallenge(str_arr):
    char_list = list(str_arr)
    char_list = list(dict.fromkeys(char_list))
    blanc_string = ''
    for char in char_list:
        blanc_string += str(str_arr.count(char))
        blanc_string += char
    return blanc_string

print(stringchallenge('aabbccddd'))
"""
