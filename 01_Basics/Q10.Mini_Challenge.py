num=int(input("Enter a Four Digit Number: "))
a=num//1000
b=(num//100)%10
c=(num//10)%10
d=num%10
total=a+b+c+d
print(total)