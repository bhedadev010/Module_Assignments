#16.Counting the frequencies in a list using a dictionary in Python.

sp= [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]

dic = {}

for i in sp:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
