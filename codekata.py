""" r=float(input())
res=2*(22/7)*r
if res<0:
    print('error')
else:
    print(round(res,2)) """

""" inp=float(input())
rnd=round(inp)
if rnd==0:
    print("Zero")
elif rnd%2==0:
    print("Even")
else:
    print("Odd") """

""" n1=input()
n2=input()
print(n1)
print(n2) """

""" a=input()
b=input()
c=input()
print(a)
print(b)
print(c) """

""" a=input()
b=input()
c=input()
print(*a,*b,*c) """

""" a=input()
b=input()
c=input()
print(a)
print(b)
print(c) """

""" a=input()
print(' '.join(a)) """

""" a=input().split(' ')
print('\n'.join(a)) """

""" name=input()
for i in name:
    print(i) """

""" name=input()
print(','.join(name))  """

""" A=input().split(' ')
print(*A) """

""" A=input().split(' ')
B=list(map(int,A))
print(*B) """

""" A=[1,2,0,3,5,0,33,7,8,0,22,45,0]  # 2 5 9

for i in A:
    if i==0:
        print(A.index(i))


for i in range(len(A)):
    if A[i]==0:
        print(i)


A=[1,2,0,3,5,0,5,33,7,8,0,22,45]

n=int(input())
for i in range(len(A)):
    if A[i]==n:
        print(i)
        break



A=-10
abs(A)

A=[1,2,3,-5,-7,-10]
B=list(map(abs,A))
B

S=[1,4,5,6,55,77,88,45,34,25,74,22,55,78]

even=[]

for i in S:
    if i%2==0:
        even.append(i)
print(even)

Even=[i for i in S if i%2==0]
Even

Odd=[i for i in S if i%2!=0]
Odd

A=input().split(' ')  # 1 2 3 4 5 / 1 2 3 4 5
B=[int(i) for i in A]
print(*B)

print(*[int(i) for i in input().split(' ')])

A=['Ram','Kumar','Raj','Krishana','Jhon','Cibi','Raja']
List3=[]
for i in A:
    if len(i)==3:
        List3.append(i)
List3

[i for i in A if len(i)==3 ]


for i in range(0,10+1):
    print(i)

i=0
while i<=5:
    print(i)
    i=i+1

i=0
while i<=5:
    i=i+1
    print(i)

i=0
while i<=25:
    i=i+2
    print(i)
    i=i+3

S=[1,4,5,6,55,77,88,45,34,25,74,22,55,78]
i=0
while i<len(S):
    print(S[i])
    i=i+1

#Break
A=[1,2,22,6,8,0,99,7,6,3,5,6,22,44,55,77]
i=0
while i<len(A):
    if A[i]==6:
        break
    else:      
        print(A[i])
    i=i+1

#Pass
A=[1,2,22,6,8,0,99,7,6,3,5,6,22,44,55,77]
i=0
while i<len(A):
    if A[i]==6:
        print('Skipping')
        i=i+1
        pass
    else:      
        print(A[i])
        i=i+1

A=[1,2,22,6,8,0,99,7,6,3,5,6,22,44,55,77]
i=0
while i<len(A):
    if A[i]==6:
        print('Skipping')
        i=i+1
        continue
    else:      
        print(A[i])
        i=i+1

import math
A=1.98
math.ceil(A)

A-math.floor(A)

A=10.019
round(A,2)

print('%.2f'%A) """

import streamlit as st
import pandas as pd 
import seaborn as sns

print(st.__version__)
print(pd.__version__)
print(sns.__version__)