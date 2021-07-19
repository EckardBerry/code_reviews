def searchingchallenge(strArr):
    holes_found = 0
    one_long_list = [char for sublist in strArr for char in sublist]
    for elem in strArr:
        for i in range(0, len(elem)-1):
            if elem[i+1] == '0' and elem[i] == '0':
                holes_found += 1
    for index in range(0, len(one_long_list) - len(strArr[0])):
        if one_long_list[index] == '0' and one_long_list[index + len(strArr[0])] == '0':
            holes_found += 1
    return f'Amount of holes found: {holes_found}'


print(searchingchallenge(['10111', '10101', '11101', '11111']))
print(searchingchallenge(['01111', '01101', '00011', '11110']))
print(searchingchallenge(['1011', '0010']))