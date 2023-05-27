""" n=input().split(' ')
num=list(n)
print(min(*num)) """

""" n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i) """


'''a,b=map(int,input().split())
arr=list(map(int,input().split()))
if b in arr:
    print('yes')
else:
    print('no') '''  

""" n=input()
a=int(n)
for i in range(1,a+1):
    print(i) """

""" l=[1,2,3]
print(l)

l.append(5)
print(l)

l.clear()
l

del l 

print(l) """

""" l1=l.copy()
print(l)
print(l1)

print(l.count(3)) """

""" l.extend([4,5,6])
print(l)

print(l.index(4))

l.insert(1,'sam')
print(l)

l.remove(5)
print(l) """

""" l.pop(2)
print(l) """

""" l=[1,2,3,4,'sam',5,6,7,'anbu',8,9] """
""" l.pop(8)
print(l)  """

l1=['sam','tom']
"""l1.pop(1)
print(l1) """
""" print(l1)

l1.remove('sam')
print(l1)

l1.reverse()
print(l1) """

""" l.reverse()
print(l) """

""" l=[1,23,4,56,78,890]
l.sort()
print(l) """

""" n=int(input())
print(n,n*2,n*3) """

""" n=int(input())
res=0.25*1.73205081*n*n
print(f'{res:.2f}') """

""" n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)
else: 
    print(n3) """

""" 1,3,5,7,8,12--31
4,6,9,11--30
2--28,29 """

""" n=int(input())
if n==1 or n==3 or n==5 or n==7 or n==8 or n==12:
    print(31)
elif n==4 or n==6 or n==9 or n==11:
    print(30)
elif n==2:
    print(28)
else:
    print('Error') """

""" n=int(input())
print(n*n*n) """

""" n1=input().split(' ')
n2=int(n1[0])
n3=int(n1[1])
for i in range(n3):
    print(n2) """

""" n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum) """

""" string=input().split()
n1=int(string[0])
n2=int(string[1])
total=n1+n2
if total%2==0:
    print('even')
else: 
    print('odd') """

""" s1=input().split(' ')
n1=int(s1[0])
n2=int(s1[1])
res=n1**n2
print(res) """

""" n=int(input())
n1=str(n)
res=' '.join(n1)
print(res) """

""" # I am shrey
#  m shry
s=input()
for i in s:
    if i in 'bcdfghjklmnopqrstvwxyzBCDFGHJKLMNOPQRSTVWXYZ':
        res=''.join(i)
        print(res,end=' ')
    elif i in 'aeiouAEIOU':
        print(' ') """

""" num=int(input('Enter a number : '))
if num%2==0:
    print('even')
else: 
    print('odd') """

""" num=float(input('Enter a number : '))
if num>0:
    print('positive number')
elif num==0:
    print('zero')
else:
    print('negative number') """

""" num=int(input('Enter a number : '))
fact=1
for i in range(1,num+1):
    fact *= i
print(f'Factorial of {num} is : {fact}') """

""" num=int(input('Enter a number : '))
rev=0
while(num>0):
    digit=num%10
    rev=(rev*10)+digit
    num=num//10
print('Reverse number is : ',rev) """

""" num=int(input('Enter a number : '))
temp=num
rev=0
while(num>0):
    digit=num%10
    rev=(rev*10)+digit
    num=num//10
if (temp==rev):
    print('Palindrome')
else:
    print('not a palindrome')
"""

""" number=input('Enter a number : ')
num=int(number)
a,b=0,1
if num<0:
    print('incorrect number entered')
elif num==0:
    print(a)
elif num==1:
    print(b)
else:
    for i in range(2,num):
        c=a+b
        a=b
        b=c
    print(f"Entered digit {num} of a fibonacci's number is : {b}") """

""" num=int(input('Choose the length of fibonacci series : '))
a=0
b=1
for i in range(1,num):
    c=a+b
    a=b
    b=c
    print(c,end=' ') """

""" def hello():
    print('Hello World')
hello() """

""" def add(a):
    return a+10
res = add(10)
print(res) """

""" def odd_even(n):
    if n%2==0:
        print('even')
    else:
        print('odd')
odd_even(13) """

""" sample = lambda a : a*a
print(sample(10)) """

""" lst=[1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda a : a%2==0,lst))
print(res) """

""" lst=[1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda i : i**3,lst))
print(res) """

""" from functools import reduce
lst=[1,2,3,4,5,6,9]
res = reduce((lambda a,b : a+b),lst)
print(res)  """

""" class Phone:
    def make_a_call(self):
        print('Making a call')
    def play_games(self):
        print('Play games')

P1 = Phone()

P1.make_a_call() """

""" from datetime import date 
class Student:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob

    def address(self):
        addr = f'name : {self.name}\ndob : {self.dob}'
        return addr 

    def age(self):
        current_year = date.today().year 
        return current_year - self.dob

stu1 = Student('sam',2000)
stu2 = Student('tom',2010)

print(stu1.name)
print(stu2.name)
print(stu1.address())
print(stu2.address())
print(stu1.age())
print(stu2.age()) """

""" class Sample():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print('name : ',self.name)
        print('age  : ',self.age)

sample1 = Sample('sam',34)
sample2 = Sample('tommy',78)
sample1.show()
sample2.show() """

""" class Sample():
    print('sam') """

""" class Sample:
    d=6
    def sam(self,a,b):
        c = a + b + self.d 
        print(c) 

sample1 = Sample()
sample1.sam(4,5) """

""" class Sample:
    d=6
    def sam(self,a,b):
        c = a + b + self.d 
        return c 

sample1 = Sample()
res = sample1.sam(4,5)
print(res) """

""" # importing About_me from a functions libraray 
# which is present in the same folder 
from functions import About_me

details = About_me('sam',89)
details.show()  """

""" num=6
for n in range(1,num+1):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c == 2:
        print(n) """

n = int(input('number : '))
s1 = list(map(int,input('numbers : ').split()))
s2 = list(map(int,input('numbers : ').split()))
l = []
res = 0
for i,j in zip(s1,s2):
    if i==j:
        l.append(i+j) 
if len(l)>=1:
    print(*l)
else:
    print(-1)

































