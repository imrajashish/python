#create  generator
def customgen(x,y):
    while x<y:
        yield x
    x+=1
result=customgen(11,22)
for i in result:print(i)
#output is not ending
#create a module and use it
import my_math 
print(my_math.sum(10,5))
print(my_math.diff(23,12))
