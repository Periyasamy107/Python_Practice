
'''   # ordered , changable , allow duplicates
list = ["sam",'lina',56,67.8,'true',90]

print(list)
print(len(list))
print(type(list))
print(list[1])
print(list[1:4])
print(list[3:])
print(list[:3])
print(list[-4:-1])
print(list[:-3])   '''

list = ["sam",'lina',56,67.8,'true','lina',90]

list[0] = 77

print(list)

list[1:4] = [1,'biggod','True',4,5,6]

print(list)
print(len(list))

list.insert(1,'god')

print(list)

a = [14,15,16,'you']
list.append(a)
list.append(678)
print(list)



