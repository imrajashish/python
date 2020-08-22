#Write a Python program to make file lists from current directory using a wildcard.
import glob
file_list = glob.glob('*.*')
print(file_list)

#Write a Python program to remove the first item from a specified list.
lst = [1,2,3,4]
print(lst.remove(2))
print(lst)
#Write a Python program to input a number, if it is not a number generate an error message.
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()

#Write a Python program to filter the positive numbers from a list.
lst = [2,-3,4,5,-65,3]
print("\n original number in the lst:",lst)
new_nums = list(filter(lambda x: x>0,lst))
print("positive number is :",new_nums)

#Write a Python program to compute the product of a list of integers (without using for loop). 
from functools import reduce
nums = [10,20,30]
nums_product = reduce((lambda x,y : x*y),nums)
print("Product of the numbers : ",nums_product)

#Write a Python program to print Unicode characters.
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print(str)