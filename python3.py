#Write a Python program to check whether a specified value is contained in a group of values.
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], 3))

#Write a Python program to concatenate all elements in a list into a string and return it.
def concatenate(list):
    result = ""
    for element in list:
        result +=str(element)
    return result

print(concatenate([1,2,3,4]))

'''Write a Python program to print all even numbers from a given numbers list in the same order and
stop the printing if any numbers that come after 237 in the sequence.'''
s = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]
for x in s:
    if x == 237:
        print(x)
        break;
    elif x%2==0:
        print(x)

#Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))#REMARK

#Write a Python program that will accept the base and height of a triangle and compute the area
x = float(input("Enter the length : "))
y = float(input("Enter the breath : "))
area = y*x/2
print("Area of tringle is : ",area)

#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
def gcd(x, y):
    gcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

print(gcd(12, 17))
print(gcd(4, 6))

#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
def sum(x,y,z):
    if x==y or y==z or z==x:
        sum = 0
    else:
      sum = x+y+z
      return True
print(sum(1,2,3))

#