s=input()
x=input()
c=0
for i in s:
    if i in x:
        c+=1
if x in s:
    print(c)
else:
    print(-1)