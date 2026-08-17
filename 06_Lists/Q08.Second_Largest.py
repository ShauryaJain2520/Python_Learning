n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
largest = None
second_largest = None
for num in numbers:
    if largest is None or num > largest:
        if num != largest:
            second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num
if second_largest is None:
    print("Second largest does not exist")
else:
    print("Largest:", largest)
    print("Second Largest:", second_largest)