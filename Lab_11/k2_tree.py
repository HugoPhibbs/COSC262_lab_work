import math

class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    point_num = 0
    box_calls = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 'P' + str(Vec.point_num)
        Vec.point_num += 1

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

    def in_box(self, bottom_left, top_right):
        """True iff this point (warning, not a vector!) lies within or on the
           boundary of the given rectangular box area"""
        Vec.box_calls += 1
        return bottom_left.x <= self.x <= top_right.x and bottom_left.y <= self.y <= top_right.y

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __lt__(self, other):
        """Less than operator, for sorting"""
        return (self.x, self.y) < (other.x, other.y)


class KdTree:
    """A 2D k-d tree"""
    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25

    def __init__(self, points: list, depth: int =0, max_depth: int =10):
        """Initialiser, given a list of points, each of type Vec, the current
           depth within the tree (0 for root), used during recursion, and the
           maximum depth allowable for a leaf node.
        """
        self.depth = depth # added this, handy when checking leaf nodes
        if len(points) < 2 or depth >= max_depth:  # Ensure at least one point per leaf
            self.is_leaf = True
            self.points = points
        else:
            self.is_leaf = False
            self.axis = depth % 2  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            points.sort(key=lambda p: p[self.axis])
            halfway = len(points) // 2
            self.coord = points[halfway - 1][self.axis]
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)

    def points_in_range(self, query_rectangle: tuple):
        """Return a list of all points in the tree 'self' that lie within or on the
           boundary of the given query rectangle, which is defined by a pair of points
           (bottom_left, top_right). bottom_left and bottom_right are Vec ojects
           depth is used when looking at leaf nodes to see if they are in the range,
           crude but a passable way to do it!
        """
        bottom_left, top_right = query_rectangle[0], query_rectangle[1]
        matches_list = []
        if self.is_leaf:
            for point in self.points:
                if point.in_box(bottom_left, top_right):
                    matches_list.append(Vec(point.x, point.y))
        else:
            # Check if the range rectangle lies to the left, right of division line or both!
            if self.chosen_x_y_coord(bottom_left) <= self.coord:
                # Traverse down the left subtree
                left_node = self.leftorbottom
                matches_list += left_node.points_in_range(query_rectangle)
            if self.chosen_x_y_coord(top_right) >= self.coord:
                # Traverse down right subtree
                right_node = self.rightortop
                matches_list += right_node.points_in_range(query_rectangle)
        return matches_list

    def point_in_range(self, point: tuple, bottom_left: Vec, top_right: Vec):
        """compares a leaf node to see if it is in the range
        point is a coordinate (x, y) tuple
        bottom left a vec for the bottom left corner of the rectangle
        top right a vec for the top right corner of the rectangle"""
        x_y_coord = point[self.depth % 2]  # Get the x or y coord, depending on the depth that this tree currently is.
        if self.depth % 2 == 0:  # Comparing x values
            return (x_y_coord >= bottom_left.x) and (x_y_coord <= top_right.x)
        else:  # Comparing y values
            return (x_y_coord >= bottom_left.y) and (x_y_coord <= top_right.y)
            # Compare x values

    def chosen_x_y_coord(self, vec: Vec) -> int:
        """Returns the coordinate of vec to compare with this tree's node, according to it's axis"""
        if self.axis == 0:
            return vec.x
        else:
            return vec.y

    def nearest_point(self, p: Vec) -> Vec:
        """Finds the nearest point to point p in a kd tree"""
        # We could just do points in range for the entire tree, but that wouldnt be all that efficient
        # 1. Find the closest point within the leaf
        # 2. Set up a rectangle area round this point based on the distance to the closest within the leaf
        # 3. Find the points in this rectangle area.
        # 4. Find the shortest distance in this rectangle area.
        # 5. If a point lies on a boundary in the rectangle area,
        #    doesnt matter, as it cant be any closer to P than the distance
        #    already found
        # 6.
        sibling_points = self.sibling_points(p)
        closest_sibling, min_sibling_distance = self.closest_point(p, sibling_points)
        query_square = self.query_square(p, min_sibling_distance)
        points_in_query_square = self.points_in_range(query_square)
        closest_point, min_distance = self.closest_point(p, points_in_query_square)
        return closest_point

    @staticmethod
    def query_square(p: Vec, min_sibling_distance: int) -> tuple:
        """Returns a tuple for the extreme coordinates of a query square used to find the point
        with the min distance from p"""
        bottom_left = Vec(p.x-min_sibling_distance, p.y-min_sibling_distance)
        top_right = Vec(p.x+min_sibling_distance, p.y+min_sibling_distance)
        return bottom_left, top_right

    @staticmethod
    def closest_point(p: Vec, points: list) -> tuple:
        """Returns the point in points which is closest to point p, along with it's
        distance to p in a tuple"""
        min_distance = float('inf')
        closest_point = None
        for point in points:
            distance = (point-p).lensq()
            if distance < min_distance:
                min_distance = distance
                closest_point = point
        if min_distance == float('inf'):
            print("min distance is infinity, must be only one point in this leaf!")
            return
        return closest_point, math.sqrt(min_distance)

    def sibling_points(self, p:tuple) -> list:
        """Traverses the tree, finding the leaf (KdTree) containing p (tuple)
         then returns the points for this leaf, which then can be used to
        find the closest point in that leaf to p"""
        # What to do if a p is the the only one in the leaf?
        sibling_points = []
        # Check if we are dealing with a leaf or a inner node
        if self.is_leaf:
            # Found a leaf
            sibling_points += self.points
        else:
            # Found an inner node
            if p[self.axis] <= self.coord:
                # Traverse the left subtree, aka left child
                left_child = self.leftorbottom
                sibling_points += left_child.sibling_points(p)
            else:
                # Traverse the right subtree, aka right child
                right_child = self.rightortop
                sibling_points += right_child.sibling_points(p)
        return sibling_points

    def plot(self, axes, top, right, bottom, left, depth=0):
        """Plot the the kd tree. axes is the matplotlib axes object on
           which to plot; top, right, bottom, left are the x or y coordinates
           the bounding box of the plot.
        """
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(p.label, (p.x, p.y),
                                  xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y))
        else:
            if self.axis == 0:
                axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth + 1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)

    def __repr__(self, depth=0):
        """String representation of self"""
        if self.is_leaf:
            return depth * 2 * ' ' + "Leaf({})".format(self.points)
        else:
            s = depth * 2 * ' ' + "Node({}, {}, \n".format(self.axis, self.coord)
            s += self.leftorbottom.__repr__(depth + 1) + '\n'
            s += self.rightortop.__repr__(depth + 1) + '\n'
            s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            return s

