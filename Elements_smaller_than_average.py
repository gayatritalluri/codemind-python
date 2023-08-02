n = int(input())
a=list(map(int,input().split()))
k =sum(a)
avg=k//n
c=[]
for i in range(n):
    if a[i]<=avg:
        c.append(i)
        
print(len(c))