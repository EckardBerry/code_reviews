def count_numbers(some_list, target):
    count = 0
    for value in some_list:
        if value < target:
            count += 1
    print(count)


count_numbers([1, 3, 5, 7], 4)