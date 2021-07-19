# Have the function StringScramble(str1,str2) take both parameters being passed and return the string true if a
# portion of str1 characters can be rearranged to match str2, otherwise return the string false.
# For example: if str1 is "rkqodlw" and str2 is "world" the output should return true. Punctuation and symbols will
# not be entered with the parameters.

def StringScramble(str1, str2):
    str2_in_str1 = False
    for char in str2:
        if char in str1:
            str2_ins_tr1 = True
        else:
            str2_in_str1 = False
            break
    print(str2_in_str1)


StringScramble('rkgodlw', 'world')