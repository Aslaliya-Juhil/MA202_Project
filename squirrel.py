from turtle import *
from bspline import bspline3, bspline1, bspline2
from util import draw, transform
points_head = [[8, 138], [8, 138], [22, 148], [55, 105], [80, 132], [52, 146], [20, 171],
               [100, 210], [153, 185], [150, 165], [
                   163, 168], [180, 140], [152, 122],
               [138, 144], [120, 92], [169, 94], [
                   265, 151], [311, 112], [324, 85],
               [313, 74], [342, 92], [320, 142], [
                   238, 161], [225, 187], [285, 212],
               [322, 212], [326, 203], [433, 201], [
                   487, 159], [487, 86], [393, 53],
               [319, 64], [316, 50], [289, 29], [
                   225, 27], [265, 53], [218, 50],
               [167, 18], [95, 6], [60, 60], [43, 105], [8, 138], [8, 138]]
points_eye = [[102, 162], [102, 162], [82, 181], [59, 170], [77, 158], [102, 162],
              [102, 162]]
points_ear = [[148, 183], [148, 183], [173, 191],
              [193, 169], [171, 157], [171, 157]]
bgcolor(0, 0, 0)
transform(points_head, 244, 106, 2)
draw(points_head, 0, (1, 0, 0), 1, 6)
transform(points_eye, 244, 106, 2)
draw(points_eye, 0, (1, 0, 0), 1, 6)
transform(points_ear, 244, 106, 2)
draw(points_ear, 0, (1, 0, 0), 1, 6)
lst_head = bspline1(points_head)
lst_eye = bspline1(points_eye)
lst_ear = bspline1(points_ear)
penup()
goto(points_head[0])
pendown()
draw(lst_head, 2, (0, 0, 1))
penup()
goto(points_eye[0])
pendown()
draw(lst_eye, 2, (0, 0, 1))
penup()
goto(points_ear[0])
pendown()
draw(lst_ear, 2, (0, 0, 1))

'''lst_head = bspline2(points_head)
lst_eye = bspline2(points_eye)
lst_ear = bspline2(points_ear)
penup()
goto(points_head[0])
pendown()
draw(lst_head, 2, (0, 1, 1))
penup()
goto(points_eye[0])
pendown()
draw(lst_eye, 2, (0, 1, 1))
penup()
goto(points_ear[0])
pendown()
draw(lst_ear, 2, (0, 1, 1))
'''
'''lst_head = bspline3(points_head)
lst_eye = bspline3(points_eye)
lst_ear = bspline3(points_ear)
penup()
goto(points_head[0])
pendown()
draw(lst_head, 2, (1, 1, 0))
penup()
goto(points_eye[0])
pendown()
draw(lst_eye, 2, (1, 1, 0))
penup()
goto(points_ear[0])
pendown()
draw(lst_ear, 2, (1, 1, 0))
'''
done()