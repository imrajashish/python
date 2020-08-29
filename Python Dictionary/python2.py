#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))

#Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
def remove_nums(int_list):
      #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)

#Write a Python program to create the combinations of 3 digit combo. 
numbers = []
for num in range(1000):
  num=str(num).zfill(3)
print(num)
numbers.append(num)
