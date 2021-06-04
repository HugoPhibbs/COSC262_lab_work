from simple_polygon import *
from helpers import *


def graham_scan(points):
    points = simple_polygon(points)
    hull_stack = [points[0], points[1], points[2]]
    for i in range(3, len(points)):
        while not is_ccw(hull_stack[-2], hull_stack[-1], points[i]):
            hull_stack.pop()
        hull_stack.append(points[i])
    return hull_stack


points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(100, 0),
    Vec(0, 0),
    Vec(49, 50)]
verts = graham_scan(points)
for v in verts:
    print(v)