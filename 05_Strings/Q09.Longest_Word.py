text = input("Enter a Sentence: ")
words = text.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest Word:", longest)