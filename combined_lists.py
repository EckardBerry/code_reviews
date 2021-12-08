def combine(list_1, list_2):
    combined_list = []

    for element in range(max(len(list_1), len(list_2))):
        if element < len(list_1):
            combined_list.append(list_1[element])
        if element < len(list_2):
            combined_list.append(list_2[element])

    return combined_list


print(combine([11,22,33], [1,2,3]))
print(combine([11,22,33], [1,2]))
print(combine([11,22], [1,2,3]))