from turtle import *


def xi(i, k, t):
    if k == 0:
        return 1
    elif k == 1:
        if i == 0:
            return 1 - t
        else:
            return t
    elif k == 2:
        if i == 0:
            return 0.5*t**2 - t + 0.5
        elif i == 1:
            return 0.5 + t*(1-t)
        else:
            return 0.5*t**2
    elif k == 3:
        if i == 0:
            return -1/6.0*t**3 + 1/2.0*t**2 - 1/2.0*t + 1/6.0
        elif i == 1:
            return 0.5*t**3 - t**2 + 2/3.0
        elif i == 2:
            return -0.5*t**3 + 0.5*t**2 + 0.5*t + 1/6.0
        else:
            return t**3/6.0


def bspline0(points):
    n = len(points)-1
    spoints = []
    for i in range(100*(n+1)+1):
        spoints.append([0, 0])
    for i in range(n+1):
        for j in range(0, 101):
            t = j/100
            spoints[100*(i)+j][0] = points[i][0]*xi(0, 0, t)
            spoints[100*(i)+j][1] = points[i][1]*xi(0, 0, t)
    return spoints


def bspline1(points):
    n = len(points)-1
    spoints = []
    for i in range(100*(n+1)+1):
        spoints.append([0, 0])
    for j in range(0, 101):
        t = j/100
        spoints[j][0] = points[0][0]*xi(0, 1, t) + points[0][0]*xi(1, 1, t)
        spoints[j][1] = points[0][1]*xi(0, 1, t) + points[0][1]*xi(1, 1, t)
    for i in range(1, n+1):
        for j in range(0, 101):
            t = j/100
            spoints[100*(i)+j][0] = points[i-1][0] * \
                xi(0, 1, t) + points[i][0]*xi(1, 1, t)
            spoints[100*(i)+j][1] = points[i-1][1] * \
                xi(0, 1, t) + points[i][1]*xi(1, 1, t)
    return spoints


def bspline2(points):
    n = len(points)-1
    spoints = []
    for i in range(100*(n+1)+1):
        spoints.append([0, 0])
    for j in range(0, 101):
        t = j/100
        spoints[j][0] = points[0][0]*xi(0, 2, t) + points[0][0]*xi(
            1, 2, t) + points[1][0]*xi(2, 2, t)
        spoints[j][1] = points[0][1]*xi(0, 2, t) + points[0][1]*xi(
            1, 2, t) + points[1][1]*xi(2, 2, t)
    for i in range(1, n):
        for j in range(0, 101):
            t = j/100
            spoints[100*(i)+j][0] = points[i-1][0]*xi(0, 2, t) + points[i][0]*xi(
                1, 2, t) + points[i+1][0]*xi(2, 2, t)
            spoints[100*(i)+j][1] = points[i-1][1]*xi(0, 2, t) + points[i][1]*xi(
                1, 2, t) + points[i+1][1]*xi(2, 2, t)
    for j in range(0, 101):
        t = j/100
        spoints[j+100*n][0] = points[n-1][0]*xi(0, 2, t) + points[n][0]*xi(
            1, 2, t) + points[n][0]*xi(2, 2, t)
        spoints[j+100*n][1] = points[n-1][1]*xi(0, 2, t) + points[n][1]*xi(
            1, 2, t) + points[n][1]*xi(2, 2, t)
    return spoints


def bspline3(points):
    n = len(points)-1
    spoints = []
    for i in range(100*n+1):
        spoints.append([0, 0])
    for j in range(0, 101):
        t = j/100
        spoints[j][0] = points[0][0]*xi(0, 3, t) + points[0][0]*xi(
            1, 3, t) + points[1][0]*xi(2, 3, t) + points[2][0]*xi(3, 3, t)
        spoints[j][1] = points[0][1]*xi(0, 3, t) + points[0][1]*xi(
            1, 3, t) + points[1][1]*xi(2, 3, t) + points[2][1]*xi(3, 3, t)
    for i in range(1, n-1):
        for j in range(0, 101):
            t = j/100
            spoints[100*(i)+j][0] = points[i-1][0]*xi(0, 3, t) + points[i][0] * \
                xi(1, 3, t) + points[i+1][0] * \
                xi(2, 3, t) + points[i+2][0]*xi(3, 3, t)
            spoints[100*(i)+j][1] = points[i-1][1]*xi(0, 3, t) + points[i][1] * \
                xi(1, 3, t) + points[i+1][1] * \
                xi(2, 3, t) + points[i+2][1]*xi(3, 3, t)
    for j in range(0, 101):
        t = j/100
        spoints[j+100*(n-1)][0] = points[n-2][0]*xi(0, 3, t) + points[n-1][0] * \
            xi(1, 3, t) + points[n][0]*xi(2, 3, t) + points[n][0]*xi(3, 3, t)
        spoints[j+100*(n-1)][1] = points[n-2][1]*xi(0, 3, t) + points[n-1][1] * \
            xi(1, 3, t) + points[n][1]*xi(2, 3, t) + points[n][1]*xi(3, 3, t)
    return spoints
