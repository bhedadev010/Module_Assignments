# 17. Write a python program using function to find  the sum of odd series and even series
#    Odd series:  12/ 1!  +   32/ 3!   +  52/ 5!+……n
#    Even series: 22/ 2!  +   42/ 4!   +  62/ 6!+……n

import math

n = 100

ev_sum=0

def os(n):
    od_sum = 0
    m = 1
    for i in range(22,n,20):
        od_sum += i / math.factorial(m)
        m+=2
    print(od_sum)

def es(n):
    ev_sum = 0
    m = 2
    for i in range(12,n,20):
        ev_sum += i / math.factorial(m)
        m+=2
    print(ev_sum)

os(n)
es(n)