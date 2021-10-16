def get_minimum_connections(matrix):
    connections = []
    airports = []
    for row in matrix:
        for element in row:
            if element == True:
                connections.append([matrix.index(row), row.index(element)])
                row[element] = ''
                airports.append(row.index(element))

    for connection in connections:
        if connection[::-1] in connections:
            connections.pop(connections.index(connection[::-1]))

    return len(set(airports)) - len(connections)


matrix = \
    [
        [False, True, False, False, True],
        [True, False, False, False, False],
        [False, False, False, True, False],
        [False, False, True, False, False],
        [True, False, False, False, False]
    ]
print(get_minimum_connections(matrix)) # should print 1