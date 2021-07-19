# Using the JavaScript language, have the function PascalsTriangle(arr) take arr which will be a
# partial row from Pascal's triangle. Pascal's triangle starts with a [1] at the first row of the triangle.
# Then the second row is [1,1] and the third row is [1,2,1]. The next row begins with 1 and ends with 1, and the
# inside of the row is determined by adding the k-1 and kth elements from the previous row. The next row in the
# triangle would then be [1,3,3,1], and so on. The input, arr will be some almost completed row from the triangle,
# for example [1,4,6,4] and your program should return the next element in that row. In this example your program
# should return 1. Another example: if arr is [1,5,10] your program should return 10. If the whole row is entered as
# input and there is no next number, your program should return -1.

# // The input array will contain at least 3 elements so [1] and [1,1] will not occur as inputs.
# // Sample Test Cases
# // Input:1,3
# // Output:3

# // Input:1,5,10,10
# // Output:5


def pascal(array):
    max_iterations = max(array)
    pascal_list = [[1], [1, 1], [1, 2, 1]]
    blank_list = []
    for iterations in range(max_iterations):
        for i in range(len(pascal_list[-1])):
            if pascal_list[-1][i] == 1:
                blank_list.append(1)
            if i == 1:
                blank_list.append((pascal_list[-1][0] + pascal_list[-1][1]))
                blank_list.append((pascal_list[-1][1] + pascal_list[-1][2]))
            elif i > 1 and pascal_list[-1][i] != 1:
                blank_list.append(pascal_list[-1][i] + pascal_list[-1][i + 1])

        pascal_list.append(blank_list)
        blank_list = []
    for lists in pascal_list:
        check = all(item in array for item in lists)
        if check is True and len(lists) >= len(array):
            print(lists[len(array)])


pascal([1, 5, 10, 10])



