n = int(input())
c=0
x=0
while n>0:
    t=n%10
    if(t%2==0):
        c+=1
    else:
        x+=1
    n=n//10
if c>0 and x==0:
    print("Even")
elif c==0 and x>0:
    print("Odd")
else:
    print("Mixed")