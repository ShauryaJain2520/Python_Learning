n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
checked = []
for num in numbers:
    if num in checked:
        continue
    count = 0
    for value in numbers:
        if value == num:
            count += 1
    print(num, "→", count)
    checked.append(num)