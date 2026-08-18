student = {
    "Name": "Rahul",
    "Age": 18,
    "Marks": 85,
    "Grade": "A"
}
key = input("Enter key to search: ")
if key in student:
    print("Key Found")
else:
    print("Key Not Found")