from turtle import *
from util import draw
from bezier import bezier_bernstein, bezier_recursive
from bspline import *

n = int(input("Number of control points : "))
points = []
for i in range(n):
    points.append(list(map(int, input("Enter the coordinates of point " +
                                      str(i+1)+" separated by a space : ").split(" "))))
bz = int(input("Bezier(1) or Bspline(2) : "))
if bz == 1:
    lst = bezier_bernstein(points)
    bgcolor(0, 0, 0)
    draw(points, 1, (1, 0, 0), 1, 6)
    penup()
    goto(points[0])
    draw(lst, 3, (0, 0, 1))
else:
    print("TBD")
done()
