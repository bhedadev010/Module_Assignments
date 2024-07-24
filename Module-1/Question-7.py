#7.	Program to find Greatest Common Divisor of two numbers.
#For example, the GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.

a = int(input("Enter A :"))
b = int(input("Enter B :"))
j = 0
af = []
bf = []

for i in range(1,int(a/2)+1):
    if a%i==0:
        af.insert(j,i)
print(af)
j = 0
for i in range(1,int(b/2)+1):
    if b%i==0:
        bf.insert(j,i)
print(bf)

x=1

for i in af:
    for j in bf:
        if i==j:
            while x==1:
                print("GCD of two numbers is : ",i)
                x-=1