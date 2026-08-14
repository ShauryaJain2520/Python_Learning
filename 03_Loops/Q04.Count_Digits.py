num=int(input("Enter a Number: "))
total=0
temp=num
count=0
while( num>0 ):
    digit=num%10
    total+=digit
    num=num/10
    count=count+1
print(count)