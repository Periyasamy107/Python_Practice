
""" i = 1 
while i <= 5:
    print('God ',i,end='')
    j = 1
    while j <= 3:
        print('  great',end='')
        j += 1
    i += 1
    print() """
    
""" i = 'samy'
j = 1
while j > 0:
    for x in i:
        print(j,i)
        j += 1
    if x == 'y':
        break
 """
""" i = 'samy'
j = 1
while j < 4:
    for x in i:
        print(j,x)
        j += 1
    if x == 'y':
        break """

""" i = 1
sum = 0 
while i <= 10:
#    if i % 2 == 0:
    sum = sum + i
    i += 1

print(sum) """

""" n = int(input('Enter a number : '))
nr = 0
while n%10!=0:
    c = n%10
    nr = nr*10 + c 
    n = n//10
print('Reverse number :',nr)
 """

""" a = [1,3.4,'sam','True']
length = 0
i = 0
try:
    while a[i]:
        length = length + 1
        i += 1
except IndexError:
    print('Length of the list is : ',length) """

""" a = int(input('Enter the number : '))
i = 1
while i<=a:
    j = 1
    while j<=i:
        print('*',end=' ')
        j+=1
    i+=1
    print() """

""" number = int(input('Enter a number :'))

count = 1
while count<=10:
    product = count*number
    print(count,'*',number,'=',product)
    count+=1 """

""" name = 'samy'

try:
    a=0
    while a <= len(name):
        print(name[a])
        a += 1
except IndexError:
    print(end='')
"""

""" i=1
while i<=10:
    print(i)
    i+=1 """


""" num=int(input('Enter a number : '))
count=0
while num!=0:
    num=num//10
    count+=1
print('Total digits are : ',count) """

""" num=int(input('Enter a number : '))
rev_number = 0
while num>0:
    rem=num%10
    rev_number=(rev_number*10)+rem 
    num=num//10
print('Reverse number is : ',rev_number) """


















