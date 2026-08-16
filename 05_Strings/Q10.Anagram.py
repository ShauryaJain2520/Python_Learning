str1 = input("Enter first String: ")
str2 = input("Enter second String: ")
str1 = str1.lower()
str2 = str2.lower()
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")