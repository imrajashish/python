#project make a file
'''class product:
    def __init__(self):
        self.name='Ashish'
        self.description='its Awsome'
        self.price='700$'
    
    p1=product()
    print(p1.name)
    print(p1.description)
    print(p1.price)'''
    class course:
        def __init__(self,name,rating):
            self.name=name
            self.rating=rating
        c1=course("java course",[1,2,3,4])
        print(c1.name)
        print(c1.rating)
        c2=course ("java web service",[5,5,5,5,5])
        print(c2.name)
        print(c2.rating)