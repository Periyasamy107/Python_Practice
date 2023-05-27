'''  print("hi")
print("i am a super dooper great and i want success in my life")
print("i am great and i want success in my life")


a = [1,2,'sam'] * 3
print(a)

list1=[8,0,9,5]
print(list1[::-1])  '''

''' i = 1
while i < 6:
    print(i)
    i += 1 '''


''' l = ['sam',76,8.90,'True']

for i in l:
    print(i) '''


'''  i = 1

while i < 6 :
    j = 1
    while j < 3 :
        print(j)
        j += 1
    i += 1  '''

""" for i in range(1,3,1):
    for j in range(10,13,1):
        print(i,'=>',j)   """

""" number = int(input('Enter a number : '))
i=1
while i<=number:
    print(i)
    i+=1
"""
""" List = [(1,2,1),(3,4,3),(5,5,6)]
for a,b,c in List:
    print(a+b+c) """

""" List = [[1,2],[2,3],[3,4]]
for i,j in List:
    print(i+j) """
""" 
n = str(456)
rev = 0
for i in n:
    digit = int(n)%10
    rev = rev*10 + digit
    num = int(n)//10

print(rev) """

""" n = 18
i = 1
odd = []
while i<=n*2:
    if i%2!=0:
        odd.append(i)
    i+=1
j = 0
for a in odd:
    j = int(a)+j
print(j)  """

""" a = int(input('enter a number : '))
arr = list(input('enter a numbers : ').split())
c = 0
for i in arr:
    if int(i)%int(i)==0:
        c+=1
    else:
        c=0
if c == 2:
    print(i) """

""" s = input('enter a string : ')
num = []
for i in s:
    if type(int(i))==int:
        num.append(i)
print(num) """

""" s = list(input().split())
l = []
for i in range(len(s)):
    if s[i] == s[i+1]:
        l.pop(s[i])
    else:
        l.append(s[i])
print(l) """

""" s = input('enter a string : ')
l = []
for i in s:
    if i == 's' or i == 'S':
        l.append(i)
if len(l)>0:
    print(len(l))
else:
    print(-1) """

""" n=15
a=[]
while(n>0):
    dig=n%2
    a.append(str(dig))
    n=n//2
res = ''.join(a)
print(res) """

""" n = list(map(str,input().split()))
c = 0
l = []
print(n[0])
print(n[1])
for i in range(len(n[0])):
    if int(i) == int(n[1]):
        l.append(int(i))
        c+=1
print(l)
if len(l)>=1:
    print(c)
else:
    print(-1) """

""" n = list(map(int,input('enter : ').split()))
s1 = list(map(str,input('enter : ').split()))
s2 = list(map(str,input('enter : ').split()))
a = ''.join(s1)
b = ''.join(s2)
if b in a:
    print('yes')
else:
    print('no') """

""" s = input('enter : ')
l = []
for i in s:
    if s.count(i)>1:
        if i not in l:
            l.append(i)
res = ''.join(l)
print(res) """

""" f = None

for i in range (5):
    with open("data.txt", "w") as f:
        if (i > 2):
            break """

""" i = 1
while True:
    if i%3 == 0:
        break
    print(i)

    i += 1 """

""" S = input('rthy  : ')
valid=False
if '@' in S:
    if S.endswith('.com'):
        if S.count('@') == 1 or S.count('&') == 1:
            valid=True
if valid == True:
    print('YES')
else:
    print('NO') """

""" n = int(input('number : '))
l = []
for n in range(1,30):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c == 2:
        l.append(i)
n = []
for m in range(1,30):
    ct=0
    for j in range(1,m+1):
        if m%j==0:
            ct+=1
    if ct == 2:
        n.append(j)
n.sort(reverse=True)
d = []
for k in l:
    for b in n:
        if k*b == n:
            d.append(k,b)

print(l)
print(n)
print(d) """

""" n = 5
s = list(map(str,input('numnret : ').split()))
l = []
m = []
for i in range(0,len(s)-1,2):
    s[i] = s[i+1]
    l.append(s[i])
    m.append(s[i+1])

res = ' '.join(s)
print(res) """

# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         else:
#             return True

# filtered = filter(prime,range(10))
# print(list(filtered))

# confusion = {}
# confusion[1] = 1
# confusion['1'] = 2
# confusion[1] += 1
# sum = 0
# for k in confusion:
#     sum += confusion[k]
# print(sum)

""" names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print(sum) """

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
res=fib(10)
print(res)



""" a,b=0,1
c=20
while c>=1:
    print(a,end=' ')
    a,b=b,a+b
    c-=1 """