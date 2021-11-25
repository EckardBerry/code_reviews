"""
# How do *args work
def foo(*args, **kwargs):
    print(*args)
    print(*kwargs)

foo(6, 7, one=1, two=2, three=3, four=4, five=5)
"""



"""
# How do **kwargs work
def foo(**kwargs):
    print(kwargs)
    print(*kwargs)


foo(one=1, two=2, three=3)
"""



"""
# What will this do?
def foo(**kwargs):
    print(kwargs)

header = {'server': '127.0.0.1', 'port': 3306, 'user': 'someone', 'password': 'pass'}
foo(**header)
"""



"""
# How would we print out the second list in the overall list?
nested_lst1 = [[1, 2], ["Venus", "Mars"], [True, False]]
"""




"""
# How would we print out only 'Venus'?
nested_lst1 = [[1, 2], ["Venus", "Mars"], [True, False]]
"""





"""
# How would we print the third dictionary only?
nested_lst2 = [{"camera": 2, "phone": 1}, {"car": 1, "van": 0}, {"Bridge": 5, "Dam": 10}]
"""




"""
# How would we print only the value of the key 'Dam'
nested_lst2 = [{"camera": 2, "phone": 1}, {"car": 1, "van": 0}, {"Bridge": 5, "Dam": 10}]
print(nested_lst2[2].get('Dam'))
"""




"""
# Print the overall list but without the commas in between
nested_lst1 = [[1, 2], ["Venus", "Mars"], [True, False]]
print(*nested_lst1)
"""




"""
# Print only the keys of the last dictionary
nested_lst2 = [{"camera": 2, "phone": 1}, {"car": 1, "van": 0}, {"Bridge": 5, "Dam": 10}]
print(*nested_lst2[2])
"""



"""
# What will be the effect of the 'zip' functionality?
nested_lst1 = [[1, 2], ["Venus", "Mars"], [True, False]]
zipped = zip(*nested_lst1)
print(list(zipped))
"""




"""
# What will the next do?  What is another way to get the value of the key 'car'?
nested_lst2 = [{"camera": 2, "phone": 1}, {"car": 1, "van": 0}]
print(nested_lst2[1]["car"])
"""




"""
# Get the color of the car in the second list item, do it in two different ways
nested_lst3 = [{"camera":{"color": "black", "res": 16}, "phone":1}, {"car": {"amount": 1, "year": 2017, "color": "red"}, "van": 0}]
#print(nested_lst3[1]["car"]["color"])
#print(nested_lst3[1].get('car').get('color'))
"""




"""
# Get the 2nd list item by name and not by index.  Also, show all the keys of the 2nd list item without the commas
nested_lst4 = {"items": {"camera": {"color": "black", "res": 16}, "phone": 1}, "assets": {"car": {"amount": 1, "year": 2017, "color": "red"}, "van": 0}}
print(nested_lst4["assets"])
print(*nested_lst4["assets"])
"""




"""
# Get only the details of a place called 'Rutland'
import requests
request = requests.get('http://api.zippopotam.us/us/vt/rutland').json()
print(request)
for dictionary in request.get('places'):
    print(dictionary.get('longitude')) if dictionary.get('place name') == 'Rutland' else None
"""