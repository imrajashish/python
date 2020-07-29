import turtle as tu
my_turtle = tu.Turtle()
my_turtle.screen.bgcolor('orange')
my_turtle.left(90)
my_turtle.speed(20)
my_turtle.color('white')
my_turtle.pensize(5)
my_turtle.screen.title("pure python")
def draw_fractal(blen):
    if(blen<10):
        return
    else:
        my_turtle.forward(blen)
        my_turtle.left(30)
        draw_fractal(3*blen/4)
        my_turtle.right(60)
        draw_fractal(3*blen/4)
        my_turtle.left(30)
        my_turtle.backward(blen)
    draw_fractal(80)
    my_turtle = tu.done()