import matplotlib.pyplot as plt

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

    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        """String representation of self"""
        return "({}, {})".format(self.x, self.y)


class QuadTree:
    """A QuadTree class for COSC262.
       Richard Lobb, May 2019
    """
    MAX_DEPTH = 20

    def __init__(self, points, centre, size, depth=0, max_leaf_points=2):
        self.size = size
        self.centre = centre
        self.depth = depth
        self.max_leaf_points = max_leaf_points
        self.children = []
        self.points = [point for point in points if self.in_square(point)]
        if len(self.points) > self.max_leaf_points and depth < self.MAX_DEPTH:
            # if the current node has too many points in it, split it into 4 children.
            self.is_leaf = False
            child_size = self.size / 2  # All children have the same size
            for quadrant in range(4):
                child_centre = self.calc_child_centre(quadrant)
                child = QuadTree(self.points, child_centre, child_size,
                                 depth+1, self.max_leaf_points)
                self.children.append(child)
        else:
            # Create a leaf
            self.is_leaf = True

    def calc_child_centre(self, quadrant: int) -> Vec:
        """Computes the child centre for a given i
        returns a vec for the child centre"""
        centre = self.centre
        size = self.size
        y_val = centre.y - ((-1) ** quadrant) * (size / 4)
        if quadrant < 2:
            x_val = centre.x - size / 4
        else:
            x_val = centre.x + size / 4
        return Vec(x_val, y_val)

    def in_square(self, point):
        """Easy to check if point is in a square, check with bounds of x vals and bounds of y vals"""
        size = self.size
        centre = self.centre
        # Find the upper and lower bounds for the square in-terms of x and y
        lower_x, upper_x = centre.x - size / 2, centre.x + size / 2
        lower_y, upper_y = centre.y - size / 2, centre.y + size / 2
        # Equals with lower bounds only
        return (lower_x <= point.x < upper_x) and (lower_y < point.y <= upper_y)

    def plot(self, axes):
        """Plot the dividing axes of this node and
           (recursively) all children"""
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
        else:
            axes.plot([self.centre.x - self.size / 2, self.centre.x + self.size / 2],
                      [self.centre.y, self.centre.y], '-', color='gray')
            axes.plot([self.centre.x, self.centre.x],
                      [self.centre.y - self.size / 2, self.centre.y + self.size / 2],
                      '-', color='gray')
            for child in self.children:
                child.plot(axes)
        axes.set_aspect(1)

    def __repr__(self, depth=0):
        """String representation with children indented"""
        indent = 2 * self.depth * ' '
        if self.is_leaf:
            return indent + "Leaf({}, {}, {})".format(self.centre, self.size, self.points)
        else:
            s = indent + "Node({}, {}, [\n".format(self.centre, self.size)
            for child in self.children:
                s += child.__repr__(depth + 1) + ',\n'
            s += indent + '])'
            return s


import matplotlib.pyplot as plt

points = [(1, 1), (99, 1), (1, 99), (99, 99),
          (49, 49), (51, 49), (49, 51), (51, 51),
          (60, 60), (70, 70), (80, 80), (90, 90)]
vecs = [Vec(*p) for p in points]
tree = QuadTree(vecs, Vec(50, 50), 100, max_leaf_points=1)
print(tree)

# Plot the tree, for debugging only
axes = plt.axes()
tree.plot(axes)
axes.set_xlim(0, 100)
axes.set_ylim(0, 100)
plt.show()