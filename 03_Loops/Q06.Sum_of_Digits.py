num=int(input("Enter a Number: "))
temp=num
total=0
while(num>0):
    digit=num%10
    total+=digit
    num=num/10
print(total)
