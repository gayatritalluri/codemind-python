def gcdd(x,y):
    i=1
    gcd=0
    while i<=x and i<=y:
        if x%i==0 and y%i==0:
            gcd=i
        i+=1
    return gcd
n=int(input())
arr=list(map(int,input().split()))
num1=arr[0]
num2=arr[1]
gcd=gcdd(num1,num2)
for i in range(2,len(arr)):
    gcd=gcdd(gcd,arr[i])
print(gcd)