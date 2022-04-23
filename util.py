from turtle import *


def draw(points, w, c, isdiscrete=0, psize=0):
    width(w)
    color(c)
    penup()
    if isdiscrete:
        for pt in points:
            goto(pt)
            pendown()
            width(psize)
            forward(1)
            back(1)
            width(w)
    else:
        pendown()
        for pt in points:
            goto(pt)
        penup()


def transform(points, dx=0, dy=0, mul=1, mat=[[1, 0], [0, 1]]):
    for pt in points:
        pt[0] -= dx
        pt[1] -= dy
        pt[0] *= mul
        pt[1] *= mul
        (pt[0], pt[1]) = (mat[0][0]*pt[0]+mat[0][1]*pt[1],
                          mat[1][0]*pt[0]+mat[1][1]*pt[1])
