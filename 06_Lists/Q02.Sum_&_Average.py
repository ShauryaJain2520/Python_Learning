n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
total = 0

for num in numbers:
    total += num
average = total / n
print("Sum:", total)
print("Average:", average)