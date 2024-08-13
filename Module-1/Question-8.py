#8.	Write a Python program to check whether a list contains a sublist.

l = [1,2,3,4,5,4,3,2]
l1 = [4,5,4]

def css(l,l1):
    for i in range(len(l) - len(l1)):
        if l[i:i + len(l1)] == l1:
            return True
    return False

print(css(l,l1))