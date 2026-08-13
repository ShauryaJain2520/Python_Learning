units=int(input("Enter Number of Units Consumed: "))
Bill=0
if(units<=100):
    Bill=units*5
elif(101<=units<=200):
    Bill=((units-100)*7)+500
elif(units>200):
    Bill=((units-200)*10)+1200
else:
    print("Invalid")
print(Bill)