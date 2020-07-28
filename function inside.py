def display(name):
    def message():
        return "Wel come to: "
    result = message()+name
    return result
print(display("Ashish"))
#Parameto to another function
'''def display(fun):
    return "hello "+ fun
def name():
    return "Ashish"
print(display(name))
#returning function
def display():
    def message():
        return "hello "
    return message
fun=display()
print(fun())
#pass
def fun(lst):
    for i in lst:
        print(i)
fun([2,3,4,5])
fun([32,34,56,78,89])
#recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return=n*factorial(n-1)'''

#cube
def cube(n):
    return n**3
print(cube(5))
#lambda
f=lambda n:n**3
print(f(3))
#Even or odd
l=lambda x:'yes' if x%2==0 else 'no'
print(l(10))
#sum
def add(a,b):
    return a+b 
print(add(10,20))
#lambda
l=lambda a,b:a+b
print(l(20,30))
#filter
lst=[10,20,30,40,11,23,32]
result=list(filter(lambda x:x%2==0, lst))
print(result)
for i in result:print(i)
#maping
l=[2,3,4,5]
result=list(map(lambda n:n*2,l))
print(result)
#reduced function
from functools import reduce
lst=[4,5,6,20,15]
result=reduce(lambda x,y: x+y,lst)
print(result)
