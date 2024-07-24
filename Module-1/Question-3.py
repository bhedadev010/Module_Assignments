#3.	Write a Python program to count the occurrences of each word in a given sentence.

n = input("Enter a sentence :")

#MOST OPTIMAL WAY

dic = dict()
sp = n.split(" ")
print(sp)

for i in sp:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

