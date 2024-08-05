#11. Write a Python program to unzip a list of tuples into individual lists.

data = [(1, 'sravan'), (2, 'ojaswi'), (3, 'bobby'), (4, 'rohith'), (5, 'gnanesh')]
data2 = list()

for i in data:
    data2.append(list(i))

print(data2)




