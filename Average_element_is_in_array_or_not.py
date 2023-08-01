n = int(input())
l = list(map(int,input().split()))
avg=sum(l)//n
for i in range(n):
    if avg==l[i]:
        print("True")
        break
else:
    print("False")