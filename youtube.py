
'''   a = 2000_000
b = 300_000
total = a + b
print(f'{total:,}')   '''

'''   name = 'tommy'

if name in ['tom','lina','malibu']:
    print('access granted!')
else:
    print('access denied!')   '''

'''   number = 56
print(number)
number = number + 4
print(number)
# above and below codes gives the same result
print(num := 56)
num += 4
print(num)   '''

'''   import math
#players must select 3 skills
skills = [
    'football',
    'vollyball',
    'table tennis',
    'badmidton',
    'basketball',
    'swimming',
    'cycling',
    'tennis',
    'boxing',
    'tickling'
]
# total no of character variations?
num_skills = len(skills)
variations = math.comb(num_skills, 3)
print('Total variations : ', variations)   '''


'''   #this code run fine
a = [1,2,3]
b = ['one','two','three']
for i in range(len(a)):
    print(a[i],':',b[i])
#this code give index error 
c = [1,2,3,4]
d = ['one','two','three']
for j in range(len(c)):
    print(c[j],':',d[j])   
#this will overcome the index error
e = [1,2,3,4]
f = ['one','two','three']
for val1,val2 in zip(e,f):
    print(val1,val2)    '''



