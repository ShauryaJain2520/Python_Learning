x=int(input("Enter First Side: "))
y=int(input("Enter Second Side: "))
z=int(input("Enter Third Side: "))
if(x+y>z or y+z>x or z+x>y):
    print("'Valid Triangle'")
    if(x==y==z):
        print("Equilateral Triangle")
    elif(x==y or y==z or x==z):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")