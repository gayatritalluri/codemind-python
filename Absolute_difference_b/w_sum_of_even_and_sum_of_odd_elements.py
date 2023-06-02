n=int(input())
l=list(map(int,input().split()))
s=0
x=0
for i in l:
  if i%2==0:
     s+=i
  else:
     x+=i
diff=abs(s-x)
print(diff)