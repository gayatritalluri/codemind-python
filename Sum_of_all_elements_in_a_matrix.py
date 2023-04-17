r,c=map(int,input().split())
mat=[]
for i in range(r):
    x=sum(list(map(int,input().split())))
    mat.append(x)
    y=sum(mat)
print(y)