"""
def factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial


print(factorial(6))
"""
def group_by_owners(files):
    from collections import defaultdict

    res = defaultdict(list)
    for key, val in sorted(files.items()):
        res[val].append(key)
    return dict(res)


if __name__ == "__main__":

    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))