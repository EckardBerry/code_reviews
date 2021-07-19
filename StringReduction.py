# Have the function StringReduction(str) take the str parameter being passed and return the smallest number you can
# get through the following reduction method. The method is: Only the letters a, b, and c will be given in str and you
# must take two different adjacent characters and replace it with the third. For example "ac" can be replaced with "b"
# but "aa" cannot be replaced with anything. This method is done repeatedly until the string cannot be further reduced,
# and the length of the resulting string is to be outputted.
# For example: if str is "cab", then "ca" can be reduced to "b" and you get "bb" (you can also reduce it to "cc").
# The reduction is done so the output should be 2. If str is "bcab", "bc" reduces to "a", so you have "aab", then "ab"
# reduces to "c", and the final string "ac" is reduced to "b" so the output should be 1.

def stringreduction(str_arr):
    find_these = {'ab': 'c', 'ba': 'c', 'ac': 'b', 'ca': 'b', 'bc': 'a', 'cb': 'a'}
    for iterate in range(0, len(str_arr)):
        for key in find_these.keys():
            str_arr = str_arr.replace(key, find_these[key])
    return len(str_arr)


print(stringreduction('bcab'))
print(stringreduction('cab'))