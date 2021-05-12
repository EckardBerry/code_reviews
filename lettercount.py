# Return the first word with the greatest number of repeating letters
# If there are no words with repeating letters return -1
# Words will be separated by spaces
'''''''''
from statistics import mode as md
def SearchingChallenge(strParam):
    empty = []
    words = strParam.split(' ')
    for word in words:
        for character in word:
            repeating = word.count(character)
            if repeating > 1:
                empty.append(word)

    if len(empty) < 1:
        print(-1)
    else:
        print(md(empty))

SearchingChallenge("Today, is the greatest day ever nevereverever!") # Should return 'nevereverever' not 'greatest'
SearchingChallenge("Hello apple pie") # Should return 'Hello'
SearchingChallenge("No words") # Should return -1
'''


'''''''''
from collections import Counter
def SearchingChallenge(strParam):
    empty = []
    words = list(strParam.split(' '))
    for word in words:
        empty.append(max(Counter(word).values()))

    result = all(value == empty[0] for value in empty)
    if result:
        return -1
    else:
        print(words[empty.index(max(empty))])

SearchingChallenge("Today, is the greatest day ever!") # Should return 'greatest'
SearchingChallenge("Hello apple pie") # Should return 'Hello'
SearchingChallenge("No words") # Should return -1
'''


def SearchingChallenge(strParam):
    empty = []
    words = strParam.split(' ')
    for word in words:
        for character in word:
            repeating = word.count(character)
            if repeating > 1:
                empty.append(word)

    if len(empty) < 1:
        print(-1)
    else:
        print(max(set(empty), key=empty.count))
        
SearchingChallenge("Today, is the greatest day ever!") # Should return 'nevereverever' not 'greatest'

