# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
""" numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)
print(numbers_plus_one) """

# Example of using a list comprehension to create a list of the numbers plus one.
""" numbers_plus_one = [number + 1 for number in numbers]
print(numbers_plus_one) """

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
""" output = []
for fruit in fruits:
    output.append(fruit.upper()) 
print(output) """
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
""" output = [fruit.upper() for fruit in fruits]
print(output) """
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
""" output=[]
for fruit in fruits:
    output.append(fruit.capitalize())
print(output) """

""" output = [fruit.capitalize() for fruit in fruits]
print(output) """
# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
""" def vowels_check(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for vowel in vowels:
        count += word.count(vowel)
    if count > 2: return True
    return False

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if vowels_check(fruit)]
print(fruits_with_more_than_two_vowels) """
# Exercise 5 - make a list that contains each fruit with more than 5 characters
""" output = [ fruit for fruit in fruits if len(fruit)>5]
print(output) """
# Exercise 6 - make a list that contains each fruit with exactly 5 characters
""" output = [ fruit for fruit in fruits if len(fruit)==5]
print(output)  """
# Exercise 7 - Make a list that contains fruits that have less than 5 characters
""" output = [ fruit for fruit in fruits if len(fruit)<5]
print(output) """
# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
""" output = [len(fruit) for fruit in fruits]
print(output) """
# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
""" output = [ fruit for fruit in fruits if 'a' in fruit]
print(output) """
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
""" output = []
for fruit in fruits:
    if len(fruit)%2==0:
        output.append(fruit)
print(output)

output1 = [ fruit for fruit in fruits if len(fruit)%2==0]
print(output1) """
# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
""" output = [ fruit for fruit in fruits if len(fruit)%2!=0]
print(output) """
# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
""" output = [ fruit for fruit in fruits if len(fruit)>0]
print(output) """
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
""" output = [ fruit for fruit in fruits if len(fruit)<0]
print(output) """
# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
""" output = [len(fruit)*2 for fruit in fruits]
print(output) """
# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
""" output = [ fruit for fruit in fruits if len(fruit)%2!=0 and len(fruit)<0]
print(output) """
# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
""" number_plus_five = [len(fruit)+5 for fruit in fruits]
print(number_plus_five) """
# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.



""" a=input('Enter a string : ')
r=0
for i in a:
    if i not in 'aeiouAEIOU':
        print(i,end='')
        r+=1
if r == 0:
    print(-1) """

""" name = 'samy is great'
print(name.split()[0]) """

""" a = input('enter a string : ')
j = 0
r = 1
x = a[j]
for i in a:
    if i == x:
        continue
    else:
        r += 1
        x = i
if r == 3:
    print('Wonder')
else:
    print(-1) """

""" a = int(input('enter the value : '))
b = list(map(str,input('enter the strings : ').split()))
c = []

for i in b:
    if i not in c:
        c.append(i)
print(*c)

#A23 B56 B56 C79 D16 """

""" # 1 6 4 0 3
n = int(input('n : '))
s = list(map(int,input('s : ').split()))
a = s.index(max(s))
b = s.index(min(s))
print(a-b) """

""" a = list(map(int,input().split()))

for i in a:
    if (a[0]%i==0) and (a[1]%i==0):
        hcf = i
print(hcf) """

""" def add(n):
    if n:
        return n+add(n-1)
    else:
        return 0
res = add(10)
print(res) """

""" a,b = 10,55
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b) """

""" def maximum(list):
    maxi = list[0]
    for i in list:
        if maxi < i:
            maxi = i
    return maxi 
print(maximum([1,20,4,-9,8])) """

""" def small_find(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
print(small_find([1,5,6,0])) """





