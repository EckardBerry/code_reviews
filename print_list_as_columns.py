def columns(list_):
    max_len = len(max(list_, key=len))
    list_ = [word.ljust(max_len) for word in list_]
    for i in range(max_len):
        print(' '.join([word[i] for word in list_]))


columns(["Write","good","code","every","day"])