n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
search = int(input("Enter element to search: "))
found = False
for num in numbers:
    if num == search:
        found = True
        break
if found:
    print("Element Found")
else:
    print("Element Not Found")