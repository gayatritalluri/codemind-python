n=input()
l=[]
y=0
for i in n:
    if i.isdigit()==True:
        l.append(i)
for i in l:
    x=int(i)
    y+=x
print(y)