#Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. 
def multiple(m, n):
    	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))

#Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
lst = [10,20,30,40,50,5,658]
print(max(lst),min(lst))

#Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
def sum_of_cubes(n):
      n -= 1
  total = 0
  while n > 0:
    total += n * n * n
    n -= 1
  return total
print("Sum of cubes: ",sum_of_cubes(3))


