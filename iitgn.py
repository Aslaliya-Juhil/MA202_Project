from turtle import *
from math import sin, pi
from util import draw, transform
from bezier import bezier_bernstein

points = [[[-50, 65], [-110, 250], [95, 275]],
          [[95, 275], [-105, 215], [-25, 60]],
          [[-25, 60], [-50, 47]],
          [[-50, 47], [-170, 122], [-225, -30]],
          [[-225, -30], [-205, 120], [-90, 105], [-50, 65]]]
circle_coord = [[185, 285]]
rad = 15
bgcolor(0, 0, 0)
color(1, 0, 0)
width(50)
forward(1)
back(1)
penup()
for i in points:
    lst = bezier_bernstein(i)
    penup()
    goto(lst[0])
    pendown()
    draw(lst, 3, (0, 0, 1))
    penup()
goto(circle_coord[0])
pendown()
width(2*rad)
color(1, 0, 0)
forward(1)
back(1)
penup()
for j in range(5):
    for i in points:
        transform(
            i, 0, 0, 1, [[sin(pi/6), -1*sin(pi/3)], [sin(pi/3), sin(pi/6)]])
        lst = bezier_bernstein(i)
        penup()
        goto(lst[0])
        pendown()
        draw(lst, 3, (0, 0, 1))
        penup()
    transform(circle_coord, 0, 0, 1, [
              [sin(pi/6), -1*sin(pi/3)], [sin(pi/3), sin(pi/6)]])
    goto(circle_coord[0])
    pendown()
    width(2*rad)
    color(1, 0, 0)
    forward(1)
    back(1)
    penup()
done()
