def isprime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if i%n==0:
            return 0
    return 1
n=int(input())
c=0
for i in range(n):
    for j in range(n):
        if i*j==n:
            if isprime(i) and isprime(j):
                print(i,end=' ')
                c+=1
if c==0:
    print('-1')