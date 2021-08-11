dd = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

def group_by_owners(dictionary):
    new_dict = dd.fromkeys(dd.values())
    empty = []
    for keyf in new_dict:
        for item in dd.items():
            if keyf in item:
                empty.append(item[0])
        new_dict[keyf] = empty
        empty = []

    return new_dict



print(group_by_owners(dd))