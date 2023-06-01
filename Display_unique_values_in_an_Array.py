n = int(input())
l =list(map(int,input().split()))
c=0
for i in l:
    x=l.count(i)
    if x==1:
        print(i,end=' ')
    else:
        c+=1
if c==n:
    print(-1)