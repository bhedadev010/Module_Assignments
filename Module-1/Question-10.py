#10. Write a Python program to get unique values from a list.

li = [1,1,1,2,2,2,3,2,1,3]
di = dict()

for i in li:
    if i in di:
        di[i]+=1
    else:
        di[i]=1

l2 = list(di.keys())
print(l2)

#OR

li = [1,2,3,4,3,2,1,2,3,4,5,6]
li = list(set(li))
print(li)