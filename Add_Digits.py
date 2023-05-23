def add(n):
    while n>9:
        n=(n%10)+(n//10)
    return n
n=int(input())
print(add(n))