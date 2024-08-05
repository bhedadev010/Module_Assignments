#13. Write a Python program to sort a dictionary (ascending /descending) by value.

from operator import itemgetter

d = {"wow": 12, "de": 16, "ew": 98, "qe": 8, "re": 74}
l1= list()
l2= list(d.items())
l2.sort(key= itemgetter(1))
print(l2)





