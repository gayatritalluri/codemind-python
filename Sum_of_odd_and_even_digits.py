n=int(input())
l=list(map(int,input().split()))
s=0
p=0
for i in range(n):
    if(i%2==0):
        s=s+l[i]
    else:
        p=p+l[i]
if s==p:
    print("YES")
else:
    print("NO")
    