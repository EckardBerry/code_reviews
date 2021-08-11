def route_exists(b_row, b_col, e_row, e_col, matrix):
    entries = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    begining = str(b_row) + str(b_col)
    finish = str(e_row) + str(e_col)
    print(entries.index(begining))
    print(entries.index(finish))





#route_exists(0, 0, 2, 2, ['road', 'not', 'not', 'road', 'road', 'not', 'not', 'road', 'road'])


