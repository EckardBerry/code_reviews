def short_path(array):
    start = 1
    empty = [array[1]]
    options = []
    for char in array[start: int(array[0])+1]:
        for tup in array[int(array[0])+1:]:
            if char in tup:
                options.append(tup[2])

        options = list(map(lambda x: array.index(x) if x in array else 0, options))
        empty.append(array[max(options)]) if array[max(options)] not in empty and array.index(empty[-1]) < array.index(array[max(options)]) else None
        options = []

    return ''.join([elem for elem in empty])


print(short_path(["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]))
print(short_path(["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]))



