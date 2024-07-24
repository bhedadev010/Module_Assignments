#5.	Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#   If the given string already ends with 'ing' then add 'ly' instead,word.
#   If the string length of the given  string is less than 3, leave it unchanged.

word = input("Enter a word :")
leng = len(word)

if leng<3:
    print(n)
else:
    if True==word.find("ing"):
        print(word.replace("ing","ly"))
    else:
        print(word.__add__("ing"))
