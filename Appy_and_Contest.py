n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    x=a/b+a/c
    if(x>=d):
        print("Win")
    else:
        print("Lose")