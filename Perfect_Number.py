n = int(input())
s = 1
for i in range(2,n//2+1):
    if(n%i == 0):
        s +=i
if( s== n):
    print("True")
else:
     print("False")