#19. Write a Python function that takes a list and returns a new list with unique
#    elements of the first list.

#make list set if you want single occurance of each item
#optimal code
def unique(li):
    l2 = list(set(li))
    print(l2)

li = [1,2,1,2,1,2,3,4,3,4,5,6,5,6]
unique(li)