"""
def monotone(some_string):
    new_string = [i for i in some_string]
    flips_to_1 = 0
    flips_to_0 = 0

    for i in range(len(new_string)-1):
        if int(new_string[i+1]) < int(new_string[i]):
            new_string[i+1] = '1'
            flips_to_1 += 1

    new_string = [i for i in some_string]
    for i in range(len(new_string)-1, 1, -1):
        if int(new_string[i-1]) > int(new_string[i]):
            new_string[i-1] = '0'
            flips_to_0 += 1

    return min(flips_to_0, flips_to_1)


print(monotone('00110'))
print(monotone('010110'))
print(monotone('00011000'))
"""


def monotone(some_string):

    new_list = [int(i) for i in some_string]
    print(new_list)
    mapped_to_1 = list(map(lambda x: for i in range(len(new_list)-1): x==1 if new_list[i+1] < new_list[i] else x, new_list))


monotone('00110')

    the_sum = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
    print(the_sum)