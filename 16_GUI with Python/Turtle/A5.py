from turtle import *

t = Turtle()
bgcolor('black')
t.pensize(2)
t.pencolor("#00e297")
color_num = 0
colors = ['#25ffbe','#00e297','#e20097']
t.speed(0)

for i in range(0,360,6):
    color_num = color_num + 1
    t.pencolor(colors[color_num])
    if color_num == 2:
        color_num = 0
    t.seth(i)
    t.circle(100)

done()