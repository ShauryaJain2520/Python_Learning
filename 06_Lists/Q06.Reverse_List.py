n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
reverse = []
for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])
print("Original:", numbers)
print("Reverse:", reverse)