from helpers import *

def intersecting(a, b, c, d):
    """Returns if two lines intersect with each other
    computes if c and d are on either side of a b
    AND if a and b are on either side of c, d"""
    return (is_ccw(a, b, c) != is_ccw(a, b, d)) and (is_ccw(c, d, a) != is_ccw(c, d, b))


a = Vec(0, 0)
b = Vec(100, 0)
c = Vec(99, 1)
d = Vec(99, -1)
print(intersecting(a, b, c, d))