text = input("Enter a Sentence: ")
result = ""
for ch in text:
    if ch != " ":
        result += ch
print("Without Spaces:", result)