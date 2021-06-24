# Challenge
# Have the function ParallelSums(arr) take the array of integers stored in
# arr which will always contain an even amount of integers, and determine how they can be split into two even
# sets of integers each so that both sets add up to the same number. If this is impossible return -1. If it's
# possible to split the array into two sets, then return a string representation of the first set followed by the
# second set with each integer separated by a comma and both sets sorted in ascending order. The set that goes first
# is the set with the smallest first integer.
# For example: if arr is [16, 22, 35, 8, 20, 1, 21, 11], then your program should output 1,11,20,35,8,16,21,22
# Hard challenges are worth 15 points and you are not timed for them.
# Sample Test Cases
# Input:1,2,3,4
# Output:1,4,2,3

# Input:1,2,1,5
# Output:-1


from itertools import combinations as cm
def parallel_sums(int_arr):
    list_of_sums = []
    list_of_perms = []
    dictionary_turned = {}
    perms = cm(int_arr, len(int_arr)//2)
    for perm in perms:
        list_of_sums.append(sum(perm))
        list_of_perms.append(tuple(sorted(perm)))
    dictionary = dict(zip(list_of_perms, list_of_sums))

    for key, value in dictionary.items():
        if value not in dictionary_turned:
            dictionary_turned[value] = [key]
        else:
            dictionary_turned[value].append(key)

    for key, value in dictionary_turned.items():
        if 1 < len(value) <= 2:
            empty_string = []
            for val in value:
                for i in val:
                    empty_string.append(i)
            print(empty_string)
            if empty_string[0] > empty_string[len(int_arr)//2]:
                print((str(empty_string[len(int_arr)//2:])) + (str(empty_string[0:len(int_arr)//2])))
            else:
                print(''.join(str(empty_string)))



print(parallel_sums([16, 22, 35, 8, 20, 1, 21, 11]))