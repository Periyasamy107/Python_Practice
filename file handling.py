
# f = open('numbers.txt','r')
""" print(f.read())
print(f.read(4))
print(f.readline())
print(f.readline(1))
 """
# for i in f:
#     print(i)

# f.close()
'''f = open('sample1.txt','r')
#print(f.read())
#print(f.read(15))
print(f.readline())
print(f.readline())
print(f.readline(1))  

for a in f:
    print(a)

f.close()   '''

# f=open('numbers.txt','r')
# f = open('numbers.txt','a')
# f.write('\n112')
# f.close()
# print(f.read())
'''   f = open('sample1.txt','a')
f.write('this is wonderful')
f.close()

f = open('sample1.txt','r')
print(f.read())   '''

'''   f = open('sample1.txt','w')
f.write('This is wonderful \t ')
f.write('samy \n')
f.write('Nice to see you \n')
f.write('Is it so.')
f.close()

f = open('sample1.txt','r')
print(f.read())   '''

# f=open('sample.txt','x')
# f.write('good to see you again and again in here')
# f.close()
# f=open('sample.txt','r')
# print(f.read())
'''   f = open('sample3.txt','x')
f.write('good to see you agin and agin in here this situation')
f.close()

f = open('sample3.txt','r')
print(f.read())   '''

'''   f = open('open_new.txt','w')
f.write('new file created by write function')
f = open('open_new.txt','r')
print(f.read())   '''

""" import os

if os.path.exists('open_new.txt'):
    os.remove('open_new.txt')

if os.path.exists('sample1.txt'):
    os.remove('sample1.txt')

if os.path.exists('sample2.txt'):
    os.remove('sample2.txt')

if os.path.exists('sample3.txt'):
    os.remove('sample3.txt') """

""" newfile = open('sample.txt','w')
newfile.write('This is my sample file')
newfile.write('\nPeriyasamy is a good boy he is smart')
newfile.write('\nhe is smart')
newfile.close() """

""" filename = 'sample.txt'
file = open(filename,'r')
data = file.readlines()
print(data)
file.close()  """

""" filename = 'sample.txt'
with open(filename,'r') as file:
    # data = file.read()
    # data = file.readline()
    data = file.readlines()
    print(data)  """

""" filename = 'newfile.txt'
with open(filename,'w') as file:
    file.write('good\n')
    file.write('nice') """

""" fruits = ['apple','orange','banana']
filename = 'newfile.txt'
with open(filename,'w') as file:
    file.writelines(fruits)  """

""" fruits = ['apple','orange','banana']
filename = 'newfile.txt'
with open(filename,'w') as file:
    for fruit in fruits:
        file.write(fruit + '\n')  """

""" fruits = ['banana','orange']
filename = 'newfile.txt'
with open(filename,'a') as f:
    for fruit in fruits:
        f.write(fruit + '\n')  """

""" filename = 'newfile.txt'
with open(filename,'a') as f:
    f.write('\n' + 'kiwi' + '\n')
    f.write('orange'+ '\n')
    f.write('strawberry' + '\n')
    f.write('orange' + '\n')  """

""" with open('newfile.txt','r') as file:
    print(file.read()) """

""" filename = 'numbers.txt'
with open(filename,'w') as file:
    for number in range(101,111):
        file.write(f'{number}\n') """

""" filename = 'numbers.txt'
with open(filename,'r') as file:
    result = file.readlines()
    result = [int(number.strip('\n')) for number in result ]
    print(result)
    print(type(result)) 
    print(sum(result)) """

""" with open('numbers.txt','w') as file:
    for number in range(101,111):
        file.write(f'{number}\n') """

""" with open('numbers.txt','r') as file:
    a = file.readlines()
    a = [int(i.strip('\n')) for i in a]
    print(a)
    print(type(a))
    print(sum(a)) """