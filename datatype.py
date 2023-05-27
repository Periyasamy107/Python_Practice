a,b = 2,5
l = []

for i in range(a,b+1):
    c = 0
    if a>1:
        for j in range(a,b+1):
            if i%j==0:
                c+=1
        if c == 1:
            l.append(i)
print(len(l))

