import turtle

my_turtle = turtle.Turtle()
count = 3

def make_a_triangle():
    for i in range(3):
        my_turtle.forward(100)   
        my_turtle.right(120)

def make_a_shape(sides, length):
    for i in range(0, sides):
        my_turtle.forward(length)
        my_turtle.right(360/sides)
