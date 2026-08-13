marks=int(input("Enter Your Marks to know your Grade: "))
if(90<=marks<=100):
    print("A")
elif(80<=marks<90):
    print("B")
elif(70<=marks<80):
    print("C")
elif(60<=marks<70):
    print("D")
elif(marks<60):
    print("F")
else:
    print("Invalid Marks")