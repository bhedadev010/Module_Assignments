#6.	Write a Python program to find the first appearance of the substring 'not' and 'poor'
#   from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
#   substring with 'good'.  Return the resulting string


# 1 way

word = "This is not bad. I am poor wow dev"
word = word.lower()

x = word.find("not")
y = word.find("poor") +3


if x and y !=-1:
    if x<y:
        for i in word:
            print(word[0:x] + "good" + word[y + 1:])
            break
    else:
        print("Words NOT nad POOR are present but not in correct order")


