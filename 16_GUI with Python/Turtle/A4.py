from turtle import *

t = Turtle()

t.pensize(1)
t.color('#ff00cc')
bgcolor('black')
t.speed(0)
t.pensize('2')

for x in range(360):
    if(x%6 == 0):
        t.seth(x)
        t.circle(100)


done()