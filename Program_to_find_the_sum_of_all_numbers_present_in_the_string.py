n=input()
l=[]
for i in n:
    if i.isdigit()==True:
        l.append(int(i))
print(sum(l))