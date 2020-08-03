#Write a Python program to solve (x + y) * (x + y).
x = 4
y = 5
s = (x + y) * (x + y)
print("output is : ",s)

#Write a Python program to add two objects if both objects are an integer type. 
x = int(input("Enter the a : "))
y = int(input("Enter the b : "))
sum = x+y
print("sum of two number is : ",sum)

# Write a Python program to display your details like name, age, address in three different lines
def personal_details():
    name , age = "Ashish",21
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
personal_details()

#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
amt = 10000
int = 3.5
years = 7
future_value  = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))       #remark


#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
x1 = float(input("Enter the number x1 is :"))
x2 = float(input("Enter the number x2 is :"))
y1 = float(input("Enter the number y1 is :"))
y2 = float(input("Enter the number y2 is :"))
distance = (x1-x2)*(y1-y2)
print("distance between the points is : ",distance)

#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
def sum(x,y):
    sum = x+y
    if sum in range(15,20):
        return 20
    else:
        return sum

print(sum(10,6))

#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
def sum(x,y):
    if x == y or abs(x+y) == 5 or x-y == 5:
        return True         #remark
    else:
        return False
print(sum(7,2))
print(sum(3, 2))
print(sum(2, 2))


#Write a Python program to check whether a file exists.
import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))    #remark
w

