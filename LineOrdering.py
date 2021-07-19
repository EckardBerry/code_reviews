# Using the JavaScript language, have the function LineOrdering(strArr) read the strArr parameter being passed
# which will represent the relations among people standing in a line. The structure of the input will be
# ["A>B","B>C","A<D",etc..]. The letters stand for different people and the greater than and less than signs
# stand for a person being in front of someone or behind someone. A>B means A is in front of B and B<C means that B is
# behind C in line. For example if strArr is: ["J>B","B<S","D>J"], these are the following ways you can arrange the
# people in line: DSJB, SDJB and DJSB. Your program will determine the number of ways people can be arranged in line.
# So for this example your program should return the number 3. It also may be the case that the relations produce an
# impossible line ordering, resulting in zero as the answer.
#
# Only the symbols <, >, and the uppercase letters A...Z will be used. The maximum number of relations strArr will
# contain is ten.   D>J>B<S

# Sample Test Cases
# Input:"A>B","A<C","C<Z"
# Output:1

# Input:"A>B","B<R","R<G"
# Output:3

from itertools import permutations
def line_ordering(str_arr):
    empty_string = ''
    construction = []
    should_append_counter = 0
    for entry in str_arr:
        if entry[0] not in empty_string:
            empty_string += entry[0]
        if entry[2] not in empty_string:
            empty_string += entry[2]
    perm = list(permutations(empty_string, len(empty_string)))

    for permutation in perm:
        for term in str_arr:
            if term[1] == '>':
                if permutation.index(term[0]) < permutation.index(term[2]):
                    should_append_counter += 1

            if term[1] == '<':
                if permutation.index(term[0]) > permutation.index(term[2]):
                    should_append_counter += 1

            if should_append_counter == len(str_arr):
                construction.append(permutation)
        should_append_counter = 0
    return len(construction)


print(line_ordering(['J>B','B<S','D>J']))
print(line_ordering(["A>B","A<C","C<Z"]))
print(line_ordering(["A>B","B<R","R<G"]))