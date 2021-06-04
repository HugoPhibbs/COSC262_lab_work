from helpers import *

def simple_polygon(points):
    anchor = bottom_most_point(points)
    return sorted(points, key=lambda p: PointSortKey(p, anchor))