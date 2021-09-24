def StringChallenge(strParam):
    indicator = False
    for char in strParam:
        if char.isalnum() and not char.isdigit():
            if '+' in strParam[:strParam.find(char)] and '+' in strParam[strParam.find(char):]:
                indicator = True
            else:
                return indicator
    return indicator

print(StringChallenge('+d+=3=+s+'))