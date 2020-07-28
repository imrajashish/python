'''num1=input("Enter the number: "))
num2=input("Enter the second number: "))
sum= float(num2)+float(num1)
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))'''
#print(sum)
def factorial(n): 
      
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
# Driver Code 
num = input("enter the number"); 
print("Factorial of",num,"is", 
factorial(num))
  