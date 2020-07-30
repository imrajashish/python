import numpy as np
x = np.array([2, 3])
y = np.array([])
print(x.size)
print(y.size)

#write a python programe to get the python version you are using
import sys
print("python version")
print(sys.version)
print("version info")
print(sys.version_info)

#diplay the current date and time
import datetime
now = datetime.datetime.now()
print("current date and time : ")
print(now.strftime("%D-%M-%Y %H:%M:%S"))#main point

#Area of circle
from math import pi
r = float(input("enter the radious of circle : "))
print("Are of circle is :"+str(r)+"is "+str(pi*r**2))#remark

#write a python programe which accept the user's first and last name and print them in reverse order with a space between them.'''

a =input("Enter the first name: ")
b =input("Enter the second name: ")

print ("hello " +str(b) + " " +str(a))

#write a python program which accepts a sequence of comma-seprated numbers from user and generte a list and tuple with those numbers
'''values= input("input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)'''

#write a python program to display the first and last colour from the following list
colour_list=["red","green","white","black"]
print("%s %s"%(colour_list[1],colour_list[-1])) 

#write a python program to display the examination sechedule
exam_st_date= (11,12,2020)
print("the date is: %i/%i/%i"%exam_st_date)  #remark

#write a python program that accepts an integer(n)and computers the valueof n+nn+nnn
n = int(input("Enter the number : "))
n1 = int("%s" %a )
n2 = int("%s%s"%(a,a))
n3 = int("%s%s%s"%(a,a,a))
print(n1+n2+n3)