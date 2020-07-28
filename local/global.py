#assign function to a variable
x=876
def display():
    x=678
    print(x)
    print(locals()['x'])
print(x)
z=display
z()
z()
#try
try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=a/b
    print(c)
except:
    print("can't divided with zero")
#string
def large_string(str,n):
    result= " "
    for i in range(n):
        result=result + str
        return result
print(large_string('f', 2))
print(large_string(' .@python_zone', 3))



 1