n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
k = int(input("Enter rotation value: "))
k = k % n
rotated = []
for i in range(n - k, n):
    rotated.append(numbers[i])
for i in range(0, n - k):
    rotated.append(numbers[i])
print("Original:", numbers)
print("Rotated:", rotated)