x = int(input())
for i in range(x):
    y = int(input())
    for j in range(y+1):
        if j*j==y:
            print("True")
            break
    else:
        print("False")