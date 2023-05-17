num = int(input())
Temp=num
sumOfDigit = 0
pro=1
while Temp > 0:
    lastDigit = Temp % 10
    sumOfDigit = sumOfDigit + lastDigit
    pro = pro * lastDigit
    Temp = Temp // 10


if (sumOfDigit==pro):
    print("Spy Number")
else:
    print("Not Spy Number")