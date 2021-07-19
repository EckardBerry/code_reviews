import re


def replace_int_delimiter(string):
    delimiter = re.findall(r"//(.*?)\n", string)
    if any(char.isnumeric() for char in delimiter):
        string = string.replace(delimiter[0], ",")
    return string


def handle_mutiple_delimiters(string):
    pattern = r"[^\[\]]+(?=\])"
    for element in re.findall(pattern, string):
        string = string.replace(element, ",")
    return string


def add(string):
    if not string:
        return 0

    string = replace_int_delimiter(string)
    string = handle_mutiple_delimiters(string)

    negatives = re.findall(r"(-\d+)", string)
    if negatives:
        raise ValueError(f"ERROR: negatives not allowed {','.join(negatives)}")

    invalid = r"[\S\s]*\D$|(?<=^)[\s\S]+(?=//)"
    if re.match(invalid, string):
        raise ValueError("ERROR: invalid input")

    if "//.\n" not in string and "." in string:
        raise ValueError("ERROR: no floats allowed")

    numbers = map(int, re.findall(r"-?\d+", string))
    numbers = filter(lambda num: num < 1000, numbers)
    return sum(numbers)