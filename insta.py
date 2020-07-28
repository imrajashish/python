'''import turtle
import time
trtl = turtle.Turtle()
trtl.pencolor('red')
trtl.pensize(5)
trtl.shape('turtle')
n=3
shapes = ['triangle','square','pentagon','hexagon','heptagon','octagon','nanogon','decagon']
while n<11:
    trtl.clear()
    for i in range(n):
        trtl.pencolor("black")
        trtl.forward(60)
        trtl.right(360/n)
    n=n+1
    trtl.penup(); trtl.home(); trtl.pendown(); trtl.penup(); trtl.home();
    trtl.pendown(); trtl.ht(); time.sleep(1); trtl.st()'''

#
import re
test_string = input("Enter string: ")

print("The original string : " + test_string)
temp = re.findall(r'\d+', test_string)
res = list(map(int, temp))

print("The number list is : " + str(res))