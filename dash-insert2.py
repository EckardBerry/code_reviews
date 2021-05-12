# Have the function DashInsertII(str) insert dashes ('-') between each two odd numbers and insert asterisks ('*')
# between each two even numbers in str. For example: if str is 4546793 the output should be 454*67-9-3.
# Don't count zero as an odd or even number.
'''''''''
def DashInsertII(string):
    blank_string = ''
    for i in range(0, len(string)):
        if i+1 >= len(string):
            blank_string += string[-1]
            break
        blank_string += string[i]
        if int(string[i]) == 0 or int(string[i+1]) == 0:
            continue
        if int(string[i]) % 2 == 0 and int(string[i+1]) % 2 == 0:
            blank_string += '*'
        if int(string[i]) % 2 != 0 and int(string[i+1]) % 2 != 0:
            blank_string += '-'

    print(blank_string)
'''

def dashinsert2(str_arr):
    print(str_arr)
    blank_string = ''
    for i in range(0, len(str_arr)):
        if i+1 >= len(str_arr):
            blank_string += str_arr[i]
            break
        blank_string += str_arr[i]
        if int(str_arr[i]) == 0 or int(str_arr[i+1]) == 0:
            continue
        if int(str_arr[i]) % 2 == 0 and int(str_arr[i+1]) % 2 == 0:
            blank_string += '*'
        if int(str_arr[i]) % 2 != 0 and int(str_arr[i+1]) % 2 != 0:
            blank_string += '-'
    print(blank_string)

dashinsert2('4546793020300')
#DashInsertII('4546793')
#DashInsertII('454679323220460803010200')