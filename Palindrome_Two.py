import string


def palindrome_two(str_arg):
    str_arg = str_arg.lower()
    special_characters = string.punctuation + ' '
    for special in special_characters:
        str_arg = str_arg.replace(special, '')

    sentence_before_reversal = [str(i) for i in str_arg]

    if sentence_before_reversal[::-1] == sentence_before_reversal:
        return 'true'
    return 'false'


print(palindrome_two('Anne, I vote more cars race Rome-to-Vienna'))


# Another way

def palindrome(word):
    reversal_of_word = list(map(lambda x: [word[x] for x in range(len(word)-1, -1, -1)], word))[0]
    if reversal_of_word == list(word):
        return True
    return False

print(palindrome('racecar'))