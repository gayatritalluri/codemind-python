n=int(input())
l=list(map(int,input().split()))
s=0
x=0
for i in range(len(l)):
  if i%2==0:
     s+=l[i]
for i in range(len(l)):
  if i%2==1:
     x+=l[i]
diff=abs(s-x)
print(diff)