
code = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..',' ' :'/', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def letters_to_morse_code(str_param):
    empty_string = ''
    for char in str_param.upper():
        if char in code.keys():
            empty_string += code[char] + ' '
    return empty_string

def morse_code_to_letters(str_param):
    str_param = str_param.split()
    empty_string = ''
    for char in str_param:
        for key, value in code.items():
            if char == value:
                empty_string += key
    return empty_string

print(letters_to_morse_code('Eckard Berry'))
print(morse_code_to_letters('. -.-. -.- .- .-. -.. / -... . .-. .-. -.-- '))