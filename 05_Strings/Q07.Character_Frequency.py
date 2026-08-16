text = input("Enter a String: ")
ch = input("Enter a Character: ")
count = 0
for c in text:
    if c.lower() == ch.lower():
        count += 1
print("Frequency:", count)