from math import sqrt
import matplotlib as plt
from k2_tree import KdTree


class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"


def in_frontier_set(p: Vec, min_distance: int, candidate: Vec):
    return (candidate.x >= p.x - min_distance)

def closest_pair(points_in):
    """Return the two closest points in the given point set.
       Precondition: points has a length >= 2.
       The return value is a tuple of two points of type Vec, sorted by
       their x values and then, if they are equal, their y values.
    """
    points = sorted(points_in, key=lambda p: (p.x, p.y))
    solution = (points[0], points[1])  # Current best point pair
    min_distance = sqrt((points[1] - points[0]).lensq())  # Current best point-pair distance

    # Construct the frontier list, which is kept sorted by y
    # **** Insert some code here to create the initial frontier list with
    # **** the first two elements of the sorted point list.

    # Now sweep the line across the point set, starting the points[2]
    i = 2

    # Points are added into the frontier list as they come. So popping from
    frontier_list = []
    while min_distance > 0 and i < len(points):
        p = points[i]
        # Remove points that no longer belong in the frontier
        while len(frontier_list) > 0:
            if not in_frontier_set(p, min_distance, frontier_list[-1]):
                frontier_list.pop()
            else:
                break

        for point in frontier_list:
            if sqrt((point - p).lensq()) < min_distance:
                min_distance = sqrt((point - p).lensq())
                solution = (point, p)

        # A full implementation would now check only frontier points with a y-value
        # within +/- d of p.y to see if any give a closer point pair. But for this
        # implementation which is using a simple Python list, you can just check
        # all frontier points.
        # *** Insert code here.
        frontier_list = [p] + frontier_list # add to the front to get O(1) performance when removing from frontier list
        i += 1

    return tuple(sorted(solution, key=lambda p: (p.x, p.y)))


# Now a test with 10,000 points.
from random import random, seed
N = 10000
SIZE = 1000000
seed(12345)
points = [Vec(int(SIZE * random()), int(SIZE * random())) for _ in range(N)]
print(closest_pair(points))