def isprime(a):
    if a<2:
        return False
    b=int(a**0.5)
    for d in range(2,b+1):
        if a%d==0:
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if isprime(i):
        c+=1
print(c)