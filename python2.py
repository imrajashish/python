#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def large_string(str,n):
    result = ""
    for i in range(n):
        result = result + str      #Remark
    return result

print(large_string("Ashish",3))
print(large_string("amit",2))

#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
x = int(input("Enter the number is : "))
if x%2==0:
    print("even number",x)
else:
    print("is odd",x) 

#Write a Python program to count the number 4 in a given list
s=(2,3,4,5,4,6,4)
print(s.count(4))

#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. 
'''def substring_copy(str, n):
      flen = 2
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))'''

#Write a Python program to test whether a passed letter is a vowel or not. 
def is_vowel(char):
    all_vowels = "a'e'i'o'u" #remark
    return char in all_vowels #remark
print(is_vowel("a"))
print(is_vowel('e'))


