s=input()
c=0
x=0
for i in s:
    if i in '0123456789':
        c+=1
if c==0:
    print(f"Doesn't contain digit")
else:
    print(f'Contains {c} digit')