import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(100)
sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.left(5)
addSquares(59)



turtle.done()