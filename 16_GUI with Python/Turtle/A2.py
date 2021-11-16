from turtle import *

t = Turtle()

bgcolor('black')
t.pensize(1)
colors = ['yellow','red','blue']

for x in range(30,360):
    t.circle(x)
    t.left(60)

    t.pencolor(colors[x%3])

done()