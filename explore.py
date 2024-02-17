# a simple dictionary
dog1 = {'name': 'December', 'breed': 'lab', 'age': 5}

# this one variable, 'dog1', stores three pieces of information
print("\nwe can access the information in a a way similar to a list, using []")
print(dog1['name'])
print(dog1['age'])

print("\nwe can access information using .get()")
print(dog1.get('name'))


print("\nwe can add more info:")
dog1.update({'plays well with others' : False})
# or more simply
dog1['smelly'] = 'always'


print("\nwe can iterate through all 'keys'")
print("This dog is decribed as:")
for k in dog1.keys():
    print(k, "is", dog1.get(k))

