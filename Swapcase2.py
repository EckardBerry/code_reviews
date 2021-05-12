
import re
def stringchallenge(str_arr):
    str_arr = str_arr.swapcase()
    original_word_list = list(str_arr.split(' '))
    print(original_word_list)
    numbers_that_need_swapping = re.findall('(\d)\S+(\d)', str_arr)
    print(numbers_that_need_swapping)
    removing_duplicates_numbers_that_need_swapping = list(map(lambda x: x if (x[1], x[0]) not in numbers_that_need_swapping else numbers_that_need_swapping.remove((x[1], x[0])), numbers_that_need_swapping))
    for tuple in numbers_that_need_swapping:
        for word in original_word_list:
            if tuple[0] in word and tuple[1] in word:
                word_list = list(word)
                word_list[word.index(tuple[0])], word_list[word.index(tuple[1])] = word_list[word.index(tuple[1])], word_list[word.index(tuple[0])]
                swapped_word = ''.join(word_list)
                original_word_list[original_word_list.index(word)] = swapped_word
    print(' '.join(original_word_list))

stringchallenge('Hello -5LoL6 lll2yy3 k6PPP5p!, 1t2')
