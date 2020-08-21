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