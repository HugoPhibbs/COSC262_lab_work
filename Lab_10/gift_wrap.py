from helpers import *

def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False

    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull

        # If the candidate results in being the start point, we have closed the convex hull
        # Hence why only exclude the last point from the convex hull
        for p in points:
            if p is hull[-1]:
                continue
            # If we just started with the scan, let candidate be the first point found
            if candidate is None:  # ** FIXME **
                candidate = p
            # Else if, the triangle formed by the last point in the hull, the canditate and the next point =
            # is a CLOCKWISE triangle, the point p lies to the right of canditate, so made p candidate, repeating
            # This process for all the points
            elif is_ccw(hull[-1], candidate, p) <= 0:
                candidate = p
        if candidate is bottommost:
            done = True  # We've closed the hull
        else:
            hull.append(candidate)

    return hull


points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
   Vec(99, 99)]
verts = gift_wrap(points)
for v in verts:
    print(v)