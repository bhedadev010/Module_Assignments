#1.	Write a python program to sum of the first n positive integers.

n = int(input("Enter N :"))
sum=0

if n>0:
    for i in range(1,n+1):
        sum+=i
    print(f"Sum of {n} integers is : {sum}")
else:
    print("You entered invalid number!")

