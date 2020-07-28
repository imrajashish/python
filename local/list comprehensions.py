#cube of number 
lst=[]
for x in range(1,11):
    lst.append(x**3)
print(lst)
#or
lst=[]
lst=[x**2 for x in range (1,11)]
print(lst)
#even number in list
lst=[x for x in range(1,11,2) if x%2==0]
print(lst)
#comman element in list
a=[2,3,4,5]
b=[23,34,56,4,5]
result=[123]
for i in a:
    if i in b:
        result.append(i)
print(result)
