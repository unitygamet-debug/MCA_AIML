person={}
person['name'] = 'Bob'
person['age'] = 21
print(person)
if 'city' in person:
    print(person['city'])

else:
    print("city not found")

del person['age']
print(person)