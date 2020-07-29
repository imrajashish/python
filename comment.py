class countdown:
    def __init__(self):
        self.a = 1
    def final(self):
        print(type(self.a))
c = countdown()
c.final()
c.final()

#what's the output
def swap(a,b):
    b,a = a,b

a,b = 2,203
swap(a,b)

print(a-b)