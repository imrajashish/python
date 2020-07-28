import math
r=input("Enter the radious")
Area=math.pi*r**2
print(Area)
#control statements
x=float(input("Enter the number: "))
if x%2==0:
    print("is even",x)
else:
    print("odd",x)
#if else ladder
x=float(input("Enter the number: "))
if x==0: print("is zero",x)
elif x%2==0: print("is even",x)
else: print("odd",x)
#while loop
while(x<=20):
    print(x)
    x+=1

#for loop
for i in range(20,500):
    print(i)
#product of number in list
lst=[10,20,30,40,50,60]
prod=1
for i in lst:
    prod*=i
    print(prod,"product is")
#table
x=input("Enter the getting table: ")
for i in range(1,11):
    print(i*x)
#break
lst=[3,67,8,9,4,6]
for i in lst:
    if(x==3):
        break
    print(i)
#Assert
x=int(input("Enter the number: "))
assert x>19,"wrong number entered"
print("U enterred",x)