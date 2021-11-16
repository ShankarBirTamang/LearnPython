from turtle import *
import turtle

window = turtle.Screen()
t = turtle.Turtle()

window.colormode(255)
t.speed(0)
t.width(2)
window.bgcolor('black')
t.pencolor('#ff006f')
t.pensize(1)

def shape(angle,side,limit):
    rd = 200
    t.forward(side)

    if side% (rd*2) == 0 :
        angle +=2
    elif side % rd == 0 :
        angle -=2
    
    t.right(angle)
    side += 2

    if side < limit :
        shape(angle,side,limit)

angle = 119
side = 0
limit = 600

shape(angle,side ,limit)
done()
