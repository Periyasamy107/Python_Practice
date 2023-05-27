

""" text = 'python'

for letters in text:
    print(letters) """

""" l = ['english','spanish','french']

for i in l:
    print(i) """

""" number = int(input('Enter a number : '))

for count in range(1,11):
    product = count * number
    print(count, '*', number, '=', product) """

""" name = 'samy'

for n in name:
    print(n) """

""" for i in range(20,10,-2):
    print(i)  """

""" for i in ['sam',56]:
    print(i) """

""" for i in ('sam',67):
    print(i) """

""" for i in 'samy':
    print(i) """

""" dictt = {
    'name':'sam',
    'age': 78
    }
print(dictt['age']) """

""" n = 5
for i in range(n):
    for j in range(n):
        print('*',end='  ')
    print() """

""" row=5
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(i,end=' ')
    print() """

""" s=0
n=int(input('enter a number : '))
for i in range(1,n+1,1):
    s+=i 
print('sum is : ',s) """

""" n=int(input('Enter a number : '))
for i in range(1,11,1):
    product=i*n 
    print(i, '*', n, '=', product) """

""" numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item>500:
        break
    elif item>150:
        continue
    elif item%5==0:
        print(item) """

""" n=5
k=5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print() """

""" n=5
a=5
for k in range(0,n+1):
    for l in range(a-k,0,-1):
        print(k,end=' ')
    print() """

""" lst=[10,20,30,40,50]
new_lst=reversed(lst)
for item in new_lst:
    print(item) """

""" lst=[10,20,30,40,50]    
size=len(lst)-1
for i in range(size,-1,-1):
    print(lst[i]) """

""" lst1=[100,90,80,70,60]
size=len(lst1)-1
for j in range(0,size+1,1):
    print(lst1[j]) """

""" for i in range(-10,0,1):
    print(i) """

""" for i in range(6):
    print(i)
else: 
    print('Done!!!') """

""" start = 25
end = 50
print("Prime numbers between", start, "and", end, "are: ")
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else: 
            print(num)  """
            
""" num1,num2=0,1
print('Fibonacci series : ')
for i in range(15):
    print(num1,end='\n')
    res=num1+num2
    num1=num2
    num2=res  """


""" list=[10,20,30,40,50,60,70,80,90,100,110,120]
for i in list[1::2]:
    print(i) """

""" n=int(input('Enter a number : '))
for i in range(1,n+1):
    print('Cube of a number is : ',(i*i*i)) """
        
""" n=int(input('Enter a number : '))
start = 2
sum_seq = 0
for i in range(0,n):
    print(start,end='+')
    sum_seq += start
    start = start * 10 + 2
print('\nsum of the above series is : ',sum_seq) """

""" rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r") """

""" my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
even = []
not_even = []
outlier = []
for i in my_list:
    if i > 90:
        outlier.append(i)    
    elif i%2 == 0:
        even.append(i)
    else:
        not_even.append(i)
print('Even numbers', even)
print('Odd numbers', not_even)
print('outliers', outlier)

mylist = [10,20,30,40,50,60,3,6,7,34,76,89]
even = []
odd = []
outlier = []
for i in mylist:
    if i > 60:
        outlier.append(i)
    elif i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Outliers : ',outlier)
print('Even numbers : ',even)
print('Odd numbers : ',odd)
 """

""" list=[6,5,4,10]
sum=0
for i in list:
    sum+=i
print('Sum is : ',sum) """

""" list=[5,67,89,6,4,32,3]
even=[]
sum=0
for i in list:
    if i%2 == 0:
        even.append(i)
for i in even:
    sum+=i 

print("Even numbers sum is : ",sum) """

""" list=[4,5,6,7,8,9,3,2,1]
count=0
for i in range(len(list)):
    if list[i]%2 == 0:
        count+=1

print('Total even number count in a list : ',count) """

""" initial_val = 0
my_list = [1,2,3,4]
cumsum = []
for i in my_list:
    initial_val += i
    cumsum.append(initial_val)
print('The cummulative sums of the list', cumsum)

initial_value = 0
list=[5,6,7,2]
sum=[]
for i in list:
    initial_value+=i
    sum.append(initial_value)

print('Cummulative sum of the list is : ',sum) """

""" state_id=[1,2,3]
state=['Tamilnadu','Kerala','Karnataka']
for i,j in zip(state_id,state):
    print(i,j)
    print(f'{i} {j}') """

""" tup=(3,'super',7.6,'good',True,5,4)
for i in tup:
    if type(i)==str:
        print(i) """

""" list_of_tup=[(1,2),(3,4)]
list1=[]
list2=[]
for i,j in list_of_tup:
    list1.append(i)
    list2.append(j)
print(list1)
print(list2) """

""" tup=(3,'star',True,4.5)
for i,j in enumerate(tup,start=1):
    #print(i,')',j)
    print(f'{i} {j}') """

""" list1=[1,2]
list2=['one','two']
list3=[True,False]
list4=[4.5,7.8]
tup=(23,34)
dict={'name':'sam','age':50}
for i,j,k,l,m,n,o in zip(list1,list2,list3,list4,tup,dict.keys(),dict.values()):
    print(i,j,k,l,m,n,o) """

""" dict={'apple':180,'banana':50,'orange':80}

for i,j in zip(dict.keys(),dict.values()):
    print(i,j) """

""" dict={'apples':180,'banana':150,'orange':100}
for i,j in dict.items():
    print(i,':',j)
    #print('Key : ',i,'Value : ',j)
    
values=[]
for i in dict.values():
    values.append(i)
    avg=sum(values)//len(values)
print('Avg is :',avg) """

""" fruits=[]
price=[]
for i in ['apples','orange']:
    fruits.append(i)
print(fruits)
for j in [200,100]:
    price.append(j)
print(price)

print(fruits,price) """

""" my_str = 'Matplotlib'
for i in my_str[0: len(my_str): 2]:
    print(i, end=' ') """

""" res = 0

for i in range(0,5):
    n = int(input("enter a  number"))
    res += n
    print(res) """

""" side = [5,4,7,8,9,3,8,2,6,4]
#area = [x*x for x in side]
for x in side:
    area = x*x
    print(area,end=' ')

#print(area) """

""" fruits=['apple','orange']
for word in fruits:
    print(word)
    for letter in word:
        print(letter)
    print() """

""" numbers=[1,2,3,4,5]
n=int(input('Enter a integer number : '))
for num in numbers:
    if n==num:
        print('Found : ',n)
        break
else: 
    print('Not Found : ',n) """

""" nums = [1, 2, 3, 4, 5, 6]
n = 7
found = False
for num in nums:
    if n == num:
        found = True
        break

print(n,found) """

""" numbers=[1,2,0,-9,-7,4,3]
sum=0
for number in numbers:
    if number<0:
        continue
    sum+=number
print('Sum on positive numbers is : ',sum) """

""" even_nums=[1,2,3,4]
total=0
for x in even_nums:
    if x % 2 == 0:
        total += x
else:
    print(f'Sum of numbers is : {total}') """

""" for j in ["hi","sam","nice","to","you"][:2]:
    print(j)  """

""" lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for i in lst:
    print("Hello!, " + i) """

""" for i in range(1,11):
    print(i) """

""" for i in range(10):
    if i%2==0:
        print(i)
"""

""" sum=0
for i in range(11):
    sum+=i
    print(sum) """

""" sum=0
for i in range(11):
    if i%2!=0:
        sum+=i
        print(sum) """

""" number=35
for i in range(1,11):
    total=i*number
    print(i ,'*' ,number ,'=', total ) """


""" # if the given range is 10
given_number = 7

for i in range(11):
        print (i," x",given_number," =",7*i) """

""" lst=[12,4,567]
for i in lst:
    print(i) """

""" number=str(84621)
count=0
for i in number:
    count+=1
print(count) """

""" str=str(input('Enter a string : '))
rev_str=''
for i in str:
    rev_str=i+rev_str
    if (str==rev_str):
        print('Yes! This is Palindrome : ',str)
    else:
        print('Not a Palindrome : ',rev_str) """

""" str=str(input("Enter a string : "))
rev_str=""
for i in str:
    rev_str=i+rev_str
print("Reverse string is : ",rev_str) """

""" number=str(input("Enter a number : "))
sum=0
for i in number:
    sum+=int(i)**3
    if sum==int(number):
        print("Yes! Amstrong number : ",sum)
    else:
        print("Not a Amstrong number : ",sum) """

""" lst=[1,34,5,66,78,34,5,62,77]
count_odd=0
count_even=0
for i in lst:
    if i%2!=0:
        count_odd+=1
        print("Total odd  number count : ",count_odd)
    else:
        count_even+=1
        print("Total even number count : ",count_even)   """

""" given_number= 7

factorial = 1
for i in range(1, given_number + 1):
    factorial = factorial * i

print("The factorial of ", given_number, " is ", factorial) """

""" str=str(input("Enter a string : "))
digits=0
letters=0
for i in str:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
print(f'Given words contains {digits} digits and {letters} letters') """

""" rangee=20
for i in range(rangee+1):
    if i%4==0 and i%5==0:
        print("FizzBuzz")
        continue
    elif i%4==0: #and i%5!=0:
        print("Fizz")
        continue
    elif i%5==0: #and i%4!=0 
        print("Buzz")
        continue
    else:
        print(i)
"""

""" 
# given list of month name
month = ["January", "April", "August","June","November"]

# iterate through each month in the list
for i in month:
    if i == "February":
            print("The month of February has 28/29 days")
    elif i in ("April", "June", "September", "November"):
            print("The month of",i,"has 30 days.")
    elif i in ("January", "March", "May", "July", "August", "October", "December"):
            print("The month of",i,"has 31 days.")
    else:
            print(i,"is not a valid month name.") """

#LOOPS PATTERN PROGRAMS
""" n=6
for i in range(1,n):
    for j in range(1,n):
        print('* ',end='')
    print()  """

""" n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()  """

""" n=6
for i in range(1,n):
    for j in range(i,n):
        print('*',end=' ')
    print() 
"""
""" n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
for i in range(1,n+1):
    for j in range(i,n+1):
        print('*',end=' ')
    print() """

""" n=6
for i in range(1,n):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(1,i+1):
        print('* ',end='')
    print()  """

""" n=6
for i in range(1,n):
    for j in range(1,i+1):
        print(' ',end=' ')
    for k in range(i,n):
        print('* ',end='')
    print() """

""" n=6
for i in range(1,n):
    for j in range(i,n-1):
        print(' ',end=' ')
    for k in range(1,i):
        print('* ',end='')
    for l in range(1,i+1):
        print('* ',end='')
    print()  """

""" n=6
for i in range(1,n):
    for j in range(1,i+1):
        print(' ',end=' ')
    for k in range(i,n-1):
        print('* ',end='')
    for l in range(i,n):
        print('* ',end='')
    print()
"""

""" n=6
for i in range(1,n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(1,i):
        print('* ',end='')
    for l in range(1,i+1):
        print('* ',end='')
    print() 
for i in range(1,n):
    for j in range(1,i+1):
        print(' ',end=' ')
    for k in range(i,n-1):
        print('* ',end='')
    for l in range(i,n):
        print('* ',end='')
    print()  """

""" n=6
for i in range(1,n):
    for j in range(1,n):
        if (j==1 or j==5): 
            print('* ',end=' ')
        else:
            print('  ',end='')
    print() """

""" n=6
for i in range(1,n):
    for j in range(1,n):
        if (i==n/2 or j==n/2+1): 
            print('* ',end=' ')
        else:
            print('  ',end='')
    print() """

""" n=6
for i in range(1,n):
    for j in range(1,n):
        if (i==j or i+j==n): 
            print('* ',end=' ')
        else:
            print('  ',end='')
    print() """

""" n=6
for i in range(1,n):
    for j in range(1,n):
        if (i==1 or j==1 or i==n-1 or j==n-1):
            print('* ',end=' ')
        else:
            print('  ',end=' ')
    print()  """

""" n=6 
for i in range(1,n):
    for j in range(1,i+1):
        if (j==1 or j==n or j==i or i==n-1):
            print('* ',end=' ')
        else:
            print('  ',end=' ')
    print() """

""" n=6
for i in range(1,n):
    for j in range(i,n):
        if (i==1 or i==n or j==n-1 or j==i):
            print('* ',end=' ')
        else:
            print('  ',end=' ')
    print() """

