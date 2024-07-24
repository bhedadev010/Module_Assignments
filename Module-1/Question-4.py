#4.	Write a Python program to get a single string from two given strings,
#   separated by a space and swap the first two characters of each string.

n = 'abc'
m = 'xyz'

l1 = [n]
l1.append(m)
na = l1[1][:2] + l1[0][2:]
nb = l1[0][:2] + l1[1][2:]
print(nb,na,end=" ")

