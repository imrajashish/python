'''lst=[]
for x in range(10,11):
    lst.append(x**1)
print(lst)

lst=[]
lst=[x**3 for x in range(1,5)]
print(lst)

lst=[x for x in range(1,21,2)]
print(lst)

lst=[x for x in range(1,21) if x%2==0]
print(lst)

a=[12,34,56,67,78,89]
b=[87,65,43,32,34,23]
result=[]
for i in a:
    if i in b:
        result.append(i)
print(result)'''

class course:
    def__init__(self,name,rating):
    self.name="Ashish"
    self.rating="4.5"

    def average(self):
        number of rating=len(self.ratings)
        average=sum(self.rating)/number of ratings
        print("average rating for",self.name,"is",average)

c1=course("java course",[5,5,5,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2=course("java web services",[32,3,44,55])
print(c2.name)
print(c2.ratings)
c2.average()
