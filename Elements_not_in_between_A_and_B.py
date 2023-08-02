n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in arr:
    if i>=a and i<=b:
        pass
    else:
        c.append(i)
if c==[]:
    print('-1')
else:
    print(*c)