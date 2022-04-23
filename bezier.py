from turtle import *


def get_params(p1, p2):
    t = 0
    lst = []
    while t <= 1:
        lst.append([t*p2[0] + (1-t)*p1[0], t*p2[1] + (1-t)*p1[1]])
        t += 0.01
    return lst


def bezier_recursive(pts):
    lst = []
    p = len(pts)
    for i in range(len(pts)-1):
        lst.append(get_params(pts[i], pts[i+1]))
    while p > 1:
        for i in range(1, len(lst)):
            for j in range(100):
                t = j * 0.01
                lst[i-1][j][0] = t * lst[i][j][0] + (1-t) * lst[i-1][j][0]
                lst[i-1][j][1] = t * lst[i][j][1] + (1-t) * lst[i-1][j][1]
        p -= 1
    return lst[0]


def C(n, i):
    if i == 0:
        return 1
    elif i > n/2:
        return C(n, n-i)
    return (n-i+1) / i * C(n, i-1)


def bernstein(n, i, x):
    return C(n, i) * x**i * (1-x)**(n-i)


def bezier_bernstein(points):
    n = len(points)-1
    bpoints = []
    for i in range(101):
        a = i/100
        (x, y) = (0, 0)
        for j in range(n+1):
            b = bernstein(n, j, a)
            x += points[j][0]*b
            y += points[j][1]*b
        bpoints.append([x, y])
    return bpoints
