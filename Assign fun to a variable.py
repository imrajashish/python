x=123
def display():
    x=678
    print(x)
    print(globals()['x'])

print(x)
z=display()
z()
z()
z()

'''def display(name):
    def message():
        return "hello"
return=message()+name
    return=result
print(display("ashish"))'''