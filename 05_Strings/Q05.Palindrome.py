text = input("Enter a String: ")
text = text.lower()
reverse = ""
for ch in text:
    reverse = ch + reverse
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")