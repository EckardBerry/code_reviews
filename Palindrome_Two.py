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
