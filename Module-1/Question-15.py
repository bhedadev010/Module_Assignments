#15.Given a number n, write a python program to make and print the list of Fibonacci series up to n.
#Input : n=7
#Hint : first 7 numbers in the series Expected output :
#First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

n = int(input("Enter N :"))
a=0
b=1
print(a,end=",")
i=0

while i!=n:
    print(b,end=",")
    a,b=b,a+b
    i=i+1