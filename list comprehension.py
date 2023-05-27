
#normal way of doing code
'''   fruits = ['orange','banana','apple','mango']

   for x in fruits:
    if 'o' in x:
        newfruit.append(x)   

print(newfruit)   '''



'''   #above same code using list comprehension

fruits = ['orange','banana','apple','mango']

numbers1 = [c for c in range(10)]
numbers2 = [d for d in range(10) if d <= 5]
newfruit1 = [a for a in fruits if 'm' in a]
newfruit2 = [b for b in fruits if b != 'apple']
newfruit3 = [e.upper() for e in fruits]
newfruit4 = [f if f != 'orange' else 'blueberry' for f in fruits]
newfruit5 = [g if g == 'umberlla' else 'redberry' for g in fruits]

print(numbers1)
print(numbers2)
print(newfruit1)
print(newfruit2)
print(newfruit3)  
print(newfruit4)
print(newfruit5)   '''

""" my_string = "hello world"
k = [(i.upper(), len(i)) for i in my_string]
print(k)

string = ['samy god']
for b in string:
    a = [b.upper(),len(b)]
print(a)

print([i.lower() for i in "HELLO"]) """
