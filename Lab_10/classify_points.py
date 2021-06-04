from helpers import *

def classify_points(line_start, line_end, points):
    """"Returns the number of points for each side of the line"""
    result_tuple = (0, 0)
    for point in points:
        if signed_area(line_start, line_end, point) > 0:
            result_tuple = (result_tuple[0], result_tuple[1]+1)
        else:
            result_tuple = (result_tuple[0]+1, result_tuple[1])
    return result_tuple

points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
   Vec(99, 99)]

print(classify_points(Vec(0, 49), Vec(100, 49), points))