from helpers import *


def is_strictly_convex(vertices):
    for i in range(len(vertices)-2):
        first = vertices[i]
        second = vertices[i+1]
        third = vertices[i+2]
        if not is_ccw(first, second, third):
            return False
    # loop back around and check triangles with the first point
    if not is_ccw(second, third, vertices[0]) \
            or not is_ccw(third, vertices[0], vertices[1]):
        return False
    return True


verts = [
    (60, 60),
    (100, 0),
    (100, 100),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))


