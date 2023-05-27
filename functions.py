
'''   def samfunction ():
 print('samy')
 print('is')        #-----------
 print('great')

samfunction()   '''

def sam (x,y):
    print(1+x)
    print('i am a great '+y)

sam(8,'person')   

'''   def nice (y):
    print('nice '+y)

nice('baby')   '''

'''   def sample1 ():
    print('sample1')

def sample2 (a):
    print(1+a)

def sample3 (b,c):
    print(b+' ' +c)

def sample4 ():
    d  = int(50) 
    e  = int(10)
    total = d / e
    print(total)

def sample5 (f,g):
    f = print('enter first value : ',f)
    g = print('enter second value : ',g)

sample1()
sample2(5)
sample3('isac','newton')
sample4()
sample5(6,6)   '''

'''   def sample (a,b):
    print(a+' '+b)

sample('good','boy')   '''

'''   list = ['pen','pencil','eraser','scale']

def samplefun (x):
    print(x*2)

samplefun(list)   '''

""" l = ['mouse  ','phone  ','laptop  ','switch  ']

def sample (x):
    print(x*3)

def fun(arg,l):
    for items in l:
        arg(items)

fun(sample,l)  """  

'''   def fun1(a,b):
    total = a + b
    print(total)

fun1(5,6)
fun1(56,8)
fun1(108,100)   '''

'''  def name():
    print('samy')
name()  '''

'''  def print_name(name):
    print('Name is : ', name)

print_name('muthu')
print_name('raj')
print_name('janu')
print_name('nagu')   '''

'''def cont():
    a = 'sam'
    for i in a:
        print(i)
cont()  '''

'''   def whil():
    a = 1
    while a <= 10:
        print(a)
        a += 2

whil()  '''

'''def lop():
    l1 = ['good','nice','great','wonderful']
    l2 = ['boy','catch','weather']
    
    for a1 in l1 :
        for a2 in l2:
             if a1 == 'great':
                break
             print(a1,a2)     
lop()   '''

'''  def samp(name,age):
    print('name is : ',name)
    print('age is  : ',age)

samp('ravith',35)
samp('guna',25)
samp('suman',98)  '''

''' def square(num):
    num * num

print(square(5))
#this logic gives as none is the output because there is no return is there  '''

'''  def square(num):
    print('hi')
    return num * num
    print('hello')
print(square(7))  '''

'''   def add():
    a = int(input("Enter first value  : "))
    b = int(input("Enter second value : "))
    c = a + b 
    print(c)

add()  '''

'''  from math import factorial

def fact(n):
    if n < 1:
        return 1
    else: 
        return ( n * factorial(n-1))

num = int(input('Enter a number : '))
print('The factorial of ', num , 'is' , fact(num))  '''

'''   a = 10  # global variable
def samp():
    b = 20  # local variable
    c = 30  # local variable
    print(a)
    print(b)
    print(c)

samp()
print(a) # this is global variable so it is get printed
print(b) # this is local  variable so it is not get printed  '''

'''
# two parameters and two arguments
def sim(a,b):
    c = a + b
    print(c)  

sim(2,3)  '''

'''
# two parameters in one is default give one or two arguments are fine here
def sam(name,age=67):
    print(name)
    print(age)
    return
sam('good',18)
sam('nice') '''

'''
#by using keyword we pass the arguments to the function
def any(num,string):
    print('This is number : ',num)
    print('This is string : ',string)
    return
any(num=12,string='nice to meet you')
any(string='wonderful',num=76)  '''

'''  #orbitrary arguments
def greetings(*friends):
    for greetings in friends:
        print('hi ',friends)

greetings('sam','lina','kali') '''

'''  def lop(*num):
    for lop in num:
        print('number : ',lop)
------------------------------------------------------------------------------------------------------
lop(1,2,3,4,5) '''

'''  #without argument without return
def add():
    a = int(input("A value is  "))
    b = int(input("B value is  "))
    c = a + b
    print('Total is : ',c)

add()  '''

'''  #with argument without return
def add(a,b):
    c = a + b
    print('Total is : ',c)

a = int(input("A value is  "))
b = int(input("B value is  "))
add(a,b)  '''

'''  #without argument with return
def add():
    a = int(input("A value is "))
    b = int(input('B value is '))
    c = a + b 
    return c 

x = add()
print('Total is ',x)  '''

'''   #with arguments with return
def add(a,b):
    c = a + b 
    return c

a = int(input('A value is '))
b = int(input('B value is '))
x = add(a,b)
print('Total is ',x)  '''

'''  def update(a):
    a = 10
    print(a)

update(8)  '''

'''  def update(a):
    print(id(a))
    a = 10
    print(id(a))
    print('a ',a)

b = 8
print(id(b))
update(b)
print('b ',b)  '''

'''  def update(list1):
    print(id(list1))
    list[1] = 100
    print(id(list1))
    print('list1 ',list1)

list = [8,9,10]
print(id(list))
print('list : ',list)
update(list)
print('list ',list)  '''

'''def add(a,b):   # parameter or formal arguments
    c = a + b
    print(c)

add(3,4)         # arguments or actual arguments  '''

''' # positional arguments
def person(name,age):
    print('Name : ',name)
    print('Age  : ',age)

print('Biggod',76)  '''

'''#keyword arguments
def person(name,age):
    print('Name : ',name)
    print('Age  : ',age)

person(name='Sam',age=45)
person(age=28,name='papanu')'''

'''#default arguments
def person(name,age=60):
    print('Name : ',name)
    print('Age  : ',age)

person(name='Sam',age=46)
person(name='lina')'''

'''#variable length arguments
def add(a,*b):
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    
    c = a 
    for i in b:
        c += i
    print(c)
add(4,5,6,7,8)'''

'''def add(*a):
    b = 0
    for i in a:
        b += i 
        print('i : ',i)
        print('b : ',b)
    return b  

x = add(4,5,6,7,8)
print('x : ',x)'''

'''# with arguments no return
def add(x,y):
    c = x + y 
    print('Addition is :',c)

a = int(input('A value is  : '))
b = int(input('B value is  : '))
add(a,b)'''

'''def greet():
    print('hi')
    print('i am here')
greet()'''

'''def greet(first_name,last_name):
    print(f'hi {first_name} {last_name}')
    print('good to see you')
greet('big','god')
greet('leone','mirchi')
'''

'''def greet(name):
    return f'hi {name}'

out = greet('god')
file = open('samp.txt','w')
file.write(out)
file.close()
file = open('samp.txt','r')

import os
if os.path.exists('sample.txt'):
    os.remove('sample.txt')

if os.path.exists('samp.txt'):
    os.remove('samp.txt')'''

'''def greet(name):
    print(f'hi {name}')

print(greet('samy'))'''

'''def increment(number,by=1):
    return number + by 

result = increment(3,4)
print(result)

print(increment(1,8))

print(increment(5,by=8))

print(increment(43))'''

'''def multiply(x,y):
    return x * y 
    
print(multiply(2,3))

def multiply1(*num):
    print(num)

multiply1(2,3,4,5)'''

'''def multiply(*num):
    for n in num:
        print(n)

multiply(2,3,4,5)'''

'''def multiply(*num):
    total = 1
    for n in num:
        total += n
        print('n : ',n)
        print('Inside total : ',total)
    return total

print('Outside total : ',multiply(2,3,4,5))'''

'''def save_user(**user): ## using parameter in double ** create the dictionary
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])

save_user(id=1,name='sam',age=34)'''

'''def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'fizz-buzz'
    if input % 3 == 0:
        return 'fizz'
    if input % 5 == 0:    
        return 'buzz'
    return input 

print(fizz_buzz(100))'''

'''def greet():
    print('hi')

greet()
greet()
greet()
greet()
greet()'''

'''def greet(name):
    print('hi',name)

greet('linda')'''

'''def add_numbers(n1,n2):
    result=n1+n2
    print('The sum is : ',result)

a = 4.5
b = 5.5
add_numbers(a,b)'''

'''def add_numbers(n1,n2):
    total = n1 + n2
    return total

a = 4.5
b = 5.5
new_variable = add_numbers(a,b)
print('The sum is : ',new_variable)'''

'''# function to find average marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

#calculate the grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 70:
        grade = 'B'
    elif average_marks >= 60:
        grade = 'C'
    elif average_marks >= 50:
        grade = 'D'
    else:
        grade = 'F'
    return grade
    
marks = [56,78,89,90,69]
average_marks = find_average_marks(marks)
print('Your average mark is : ',average_marks)

grade = compute_grade(average_marks)
print("Your grade is : ",grade)'''

'''#add_numbers
def add_nummbers(n1,n2):
    addition = n1 + n2 
    return addition 

#multiply_numbers
def multiply_numbers(x,y):
    multiply = x * y
    return multiply
    
a = 4
b = 5
add_result = add_nummbers(a,b)
print('Addition is : ',add_result)

mul_result = multiply_numbers(a,b)
print('Multiply is : ',mul_result)'''

'''def greet_mark():
    print('Hi Mark')

def greet_john():
    print('Hi John')

def greet_lina():
    print('Hi Lina')

greet_john()
greet_lina()
greet_mark()'''

'''def greet_customer(name,age):
    print('your name is : '+name)
    print('your age is  :',age)

greet_customer('sam',54)
greet_customer('lina',37)
greet_customer('sumpana',19)'''

'''def fun1():
    print('hi')

print('good')
fun1()'''

'''def fun2(x):
    return x * 3

print(fun2(5))
print(fun2(3))'''

'''def fun3(x):
    print('start')
    print(x)
    return 4 * x

res = fun3(2)
print('finish')
print(res)'''

'''def bmi_calc(name,weight_kg,height_cm):

    bmi = weight_kg / (height_cm ** 2) * 10000
    print('bmi : ',bmi)
    if bmi<18.5:
        return name + ' you are less weight'
    elif bmi <= 25:
        return name + ' you are in perfect weight'
    return name + ' you are overweight so you need to do workout'

a = str(input('Enter your name    : '))
b = float(input('Enter your weitht  : '))
c = float(input('Enter your height  : '))
let_us_see_the_weight = bmi_calc(a,b,c)
print(let_us_see_the_weight)
'''

""" def convert(miles):
    km = 1.6 * miles
    return km

sam_variable = int(input('km is : '))
res = convert(sam_variable)
print('m  is :',res) """

""" def jani(mood='happy'):
    if mood == 'happy':
        print('I am happy')
    else:
        print('**********')

a = 56
jani(a)
jani() """

""" def sample(x):
    while(x<=10):
        print('number : ',x)
        x += 1
    return x
        
a = int(input('Enter number : '))
res = sample(a)
print('\nresult : ',res) """

""" def sample(x):
    if x<=10:
        while(x<=15):
            print('number : ',x)
            x += 1
    return x
        
a = int(input('Enter number : '))
res = sample(a)
print('\nresult : ',res) """

""" def hello_func():
    i = 1 
    while(i<=5):
        print('hi')
        i += 1

hello_func() """

""" def sam():
    return 'beautiful'

res = sam().upper()
print(res)
 """
""" 
def hello_fun(greeting,name='there'):
    return '{},,, {}'.format(greeting,name)

print(hello_fun('hi'))
print(hello_fun('hi','gooooooood'))
 """

"""  
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('mark','anthony',56,'true',78.9,age=45,interest='watch tv',true='yes')
 """

'''def fun(*sam1,**sam2):
    print(sam1)
    print(sam2)

course = ['list','ok']
info   = {'name':'sam','age':'36'}

fun(course,info)'''

""" def fun(*sam1,**sam2):
    print(sam1)
    print(sam2)

course = ['list','ok']
info   = {'name':'sam','age':'36'}

fun(*course,**info) """

'''print('{0} {1}'.format('nice','weather'))

a = 'Are you'
b = 'boy?'
print('{0} good {1}'.format(a,b))'''

""" 
#format type of printing the statements
number1 = int(input('Enter number one  : '))
number2 = int(input('Enter number two  : '))
print('Entered number1 :',format(number1))
print('Entered number2 :',format(number2))
total = number1 + number2
print('Total value of {} and {} is : {}'.format(number1,number2,total)) 

number1 = int(input('Enter number one  : '))
number2 = int(input('Enter number two  : '))
total = number1 + number2
print(f'Total value of {number1} and {number2} is : {total}')  """

'''name = str(input('Enter your name : '))
print(f'Your name is : {name.upper()}')'''
'''age = int(input('Enter your age : '))
print(f'Your age is : {age}')'''

""" 
#number of days in month. first placeholder for indexing purposes.
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    #return true for leap years , false for non-leap years
    return year%4==0 and (year%100!=0 or year%400==0)
    '''if year%4==0:
        return 'true'
    if year%100!=0 or year%400==0:
        return 'false'''

def days_in_month(year,month):
    #return number of days in that month in that year
    if not 1<=month<=12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2020))
print(days_in_month(2021,9))
"""

""" def max_of_two(x,y):
    if x > y:
        return x 
    return y 

def max_of_three(x,y,z):
    return max_of_two(max_of_two(x,y),z)

#max_value = max_of_three(5,67,900)
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
print(f'Max value out of {a},{b},{c} is : {max_of_three(a,b,c)}')
"""

""" def mul(numbers):
    total = 1
    for x in numbers:
        total *= x 
    return total

a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
list = [a,b,c]
res = mul(list)
print(f'Multiply value out of {a},{b},{c} is : {res}') """

""" def duplicateEliminator(l):
    return set(l)

a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
d = int(input('d : '))
l = [a,b,c,d]
res = duplicateEliminator(l)
print('Duplicate eliminated list : ',res) """

""" def squareMachine(l):
    i = 0
    while i<len(l):
        l[i] = l[i] ** 2
        print(i)
        print(l[i])
        i += 1
    return l 
a = [3,6,9,10]
print(a)
res = squareMachine(a)
print(res) """

""" def dictdecomposer(dict):
    print(f'The keys of the dictionary are {list(dict.keys())}')
    print(f'The values of the dictionary are {list(dict.values())}')

dictionary = {
    'FirstName' : 'Big',
    'SecondName' : 'God'
}

dictdecomposer(dictionary) """

""" import random

def guess(a):
    random_number = random.randint(1,a)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Enter a number between 1 and {a} : '))
        if guess<random_number:
            print('too low')
        elif guess>random_number:
            print('too high')
    print(f'you guessed correct number : {random_number}')

guess(100)  """ 

""" import random

def guess(a):
    ran_number = random.randint(1,a)
    guess=0
    while guess!=ran_number:
        guess=int(input(f"Enter a number between 1 and {a} : "))
        if guess<ran_number:
            print("Your guess is low")
        elif guess>ran_number:
            print("Your guess is high")
    print("You guessed a correct number : ",ran_number)    

guess(10)  """           

""" # this class share its library to practice
# which is present in the same folder
class About_me:

    def __init__(self,name,age):
        self.name = name
        self.age  = age 

    def show(self):
        print('name : ',self.name)
        print('age  : ',self.age)

sam = About_me('dummy',00)
sam.show()
 """


""" def samp():
    for i in range(5):
        print(i)
    else:
        print('success 1')

samp()

def sam():
    for j in range(5):
        print(j)
        if j == 3:
            break
    else:
        print('success 2')

sam() """

""" def utter():
    for k in range(5):
        if k == 2:
            continue
        print(k)
    else: 
        print('success 3')

utter()

def sam():
    i = [1,2,3,4,5,6]
    for a in i:
        if a == 3:
            continue
        print(a)

sam() """













