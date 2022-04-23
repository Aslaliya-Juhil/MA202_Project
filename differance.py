from turtle import *
from bspline import bspline3
from bezier import bezier_bernstein
from util import draw

points = [[-300, -300], [-300, -100], [-300, 100],
          [-100, 300], [100, 400], [400, 400],
          [400, 100], [300, -100], [100, -300],
          [-100, -300], [-300, -300]]
pointsm = [[-300, -300], [-300, -100], [-300, 100],
           [-100, 300], [100, 400], [500, -100],
           [400, 100], [300, -100], [100, -300],
           [-100, -300], [-300, -300]]
choice = int(input("Bezier(-ve number) or B-spline(+ve number or 0)? : "))
if choice < 0:
    lst = bezier_bernstein(points)
    lstm = bezier_bernstein(pointsm)
    bgcolor(0, 0, 0)
    draw(points, 1, (1, 0, 0), 1, 6)
    draw(lst, 3, (0, 1, 0))
    draw(pointsm, 1, (1, 1, 0), 1, 6)
    draw(lstm, 3, (0, 0, 1))
else:
    lst = bspline3(points)
    lstm = bspline3(pointsm)
    bgcolor(0, 0, 0)
    draw(points, 1, (1, 0, 0), 1, 6)
    draw(lst, 3, (0, 1, 0))
    draw(pointsm, 1, (1, 1, 0), 1, 6)
    draw(lstm, 3, (0, 0, 1))
done()
