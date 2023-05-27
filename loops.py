
'''   n = [1,2,3,4,5]
for a in n:
    print(a)   '''

'''   name = ['sam','latha','deena','lina']
for n in name:
    print(name[0])
    print(name[1])
    print(name[2])
    print(name[3],'\n')   '''

'''   string1 = 'biggod'
for s in string1:
    print(s)   '''

'''   n = [1,2,3,4,5,6,7]

for a in n:
    print(a)
   if a >= 4:
        break   '''

'''   n = [1,2,3,4,5]

for a in n:
    if a == 2 or a == 3:
        continue
    print(a)   '''

'''   for a in range(5):
    print(a)   '''

'''   for a in range( 20 , 30 ):
    print(a)   '''

'''   # Ways to increment by 2,3,4,5,....
# 1) Range method
    
x = [1,2,3,4,5,6,7,8,9,10]
for a in range(0,len(x),4):
    print(a)

# 2) while loop

y = 10
while y <= 20:
    print(y)
    y += 3   '''

'''   i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1   '''

'''   i = 0
while i <= 4:
    i += 1
    if i == 3:
        continue
    print(i)   '''

'''   x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)   '''

'''   i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1   '''


""" fruits=['apple','banana','orange','pineapple','lemon']
new_fruits=[]
for fruit in fruits:
    if fruit!='orange':
        new_fruits.append(fruit)
    else:
        new_fruits.append('Nofruit')
print(new_fruits) """
    
name_list = ['a','b',12,1,3,'c','d','e']
new_name_list = []
for name in name_list:
    if name not in [0,1,2,3,4,5,6,7,8,9]:
        new_name_list.append(name)
    else : 
        new_name_list.append('samy')
print(new_name_list)

    
    