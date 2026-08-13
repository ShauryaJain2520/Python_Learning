x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
z=int(input("Enter Third Number: "))
if(x>=y and x>=z):
    print(x)
elif(y>=z and y>=x):
    print(y)
elif(z>=x and z>=y):
    print(z)
else:
    print("All are Equal")