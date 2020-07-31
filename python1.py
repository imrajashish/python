#Write a python programe to print the calander of using month and year
import calendar
x = int(input("Enter the year : "))
y = int(input("Enter the month : "))
print(calendar.month(x,y))

#Write a Python program to print the following here document
print('''i am ashish
     i am in b.tech.
     3red yera student''')

#Write a Python program to calculate number of days between two dates
from datetime import date
f_d1 = date(2015,12,30)
f_d2 = date(2015,10,30)
dal = f_d1-f_d2
print("Total numbers of days :",dal.days)

#Write a Python program to get the the volume of a sphere with radius 6.
r=float(input("Enter the radious is : "))
pi=3.14
v=4.0/3.0*pi*r**3
print("volume of sphere is :",v)
#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))
#Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def sum_thrice(x, y, z):
    
     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
