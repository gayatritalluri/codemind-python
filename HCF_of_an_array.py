x=int(input())
a=list(map(int,input().split()))
d=max(a)
for j in range(d,0,-1):
    c=0
    for i in range(x):
        if(a[i]%j==0):
            c+=1
    if(c==x):
        print(j)
        break