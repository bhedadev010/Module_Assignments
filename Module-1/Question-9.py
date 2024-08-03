#9.	Write a Python program to find the second smallest number in a list.

n = [1,1,1,3,3,4,2,2,3,2,1]
n.sort()
i=1

while(True):
    if n[i]==n[i+1]:
        i+=1
    else:
        break

a=n.count(n[i])

if a==1:
    print(n[i])
else:
    print(n[i+1])