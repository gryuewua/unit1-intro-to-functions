import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
for x in range(60):
    t.right(5)
    for y in range(4):
        t.forward(100)
        t.left(90)


turtle.done()