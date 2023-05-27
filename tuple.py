
'''   # ordered, unchageable, allow duplicate

tup = ('list',45,'true',98)

print(tup)
print(type(tup))
print(tup[1:3])
print(tup[2:4])

a = list(tup)
a[1:2] = [3456,'good','wonderful',900]
b = tuple(a)

print(b)   '''


tuple1=(5,1,7,6,2)

tuple1.pop(2)

print(tuple1)







