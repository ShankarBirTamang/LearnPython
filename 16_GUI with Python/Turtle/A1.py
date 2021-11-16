from turtle import *

t = Turtle()

bgcolor('black')
t.pencolor('yellow')
t.pensize(1)

for x in range(360):
    t.forward(x)
    t.left(50)

done()