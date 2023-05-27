
""" # unordered, unchangable , not allow duplicates

dictt = {
    'name' : 'sam' ,
    'age'  : 38 ,
    'gender' : 'male' ,
    'interest' : ['playing','sleeping',1000]
} 

# Keys don't allow the duplicate but values can allow the duplicates

print(dictt)
#printing the value in two methods
print(dictt['gender'])
print(dictt.get('gender'))
#above two methods are print in python
print(dictt['interest'])
print(len(dictt))
# two methods of updating the values
# 1) normal method
dictt['age'] = 10
print(dictt)
# we can update only one value at a time
# 2) update method
dictt.update({'gender':'male111','interest':'nothing'})
print(dictt)
# by update method we can update more than one value at a time

dictt['color'] = 'red' 
print(dictt)

dictt.pop('gender')
print(dictt)  """

dictionary = {1:'apple',2:'orange',3:'banana'}

print(dictionary[3])

print(dictionary[2])

print(dictionary.keys())

print(dictionary.values())

print(dictionary.items())

















