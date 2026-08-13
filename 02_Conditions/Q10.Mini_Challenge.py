age=int(input("Enter a Age: "))
if(0<age<=12):
    print("Child")
elif(13<=age<18):
    print("Teenager")
elif(18<=age<60):
    print("Adult")
elif(age>=60):
    print("Senior Citizen")
else:
    print("Invalid")
if(18<=age):
    Citizenship=input("Choose your Citizenship 'Indian or Other':")
    if(Citizenship=='Indian'):
        print("You are Eligible to Vote ")
    else:
        print("Sorry, You are not Eligible to Vote ")

