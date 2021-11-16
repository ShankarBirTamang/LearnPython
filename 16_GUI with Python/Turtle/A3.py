from turtle import *

t = Turtle()

t.pensize(1)
t.color('yellow')
bgcolor('black')
t.speed(0)

for x in range(0,360,3):
    t.seth(x)
    t.circle(100)

done()