#14. Write a Python program to find the highest 3 values in a dictionary.

a = {"wow":3, "gg":5, "nice":8, "noice":10,"what":8}
print(a)
l1 = list(a.values())
l1.sort(reverse=True)
n = l1[0:3]
b = list()

for i in a:
    for j in n:
        if j == a[i]:
            b.append(i)

b = set(b)
print(b)