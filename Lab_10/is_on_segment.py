from vec import Vec


def is_on_segment(p, a, b):
    p_a = a-p
    p_b = b-p
    a_b = b-a
    return signed_area(p, a, b) == 0 and \
           (p_a.lensq() <= a_b.lensq() and p_b.lensq() <= a_b.lensq())


def signed_area(a, b, c):
    """Calculates the signed area of the given 3 points"""
    p = b-a
    q = c-a
    return p.x*q.y-q.x*p.y

a = Vec(0, 0)
b = Vec(1000, 2000)
point_tuples = [
    (-1, -1),
    (-1, -2),
    (-1000, -2000),
    (0, 0),
    (1, 2),
    (500, 1000),
    (500, 1001),
    (500, 999),
    (1000, 2000),
    (1001, 2001),
    (1001, 2002),
    (2000, 4000)]
points = [Vec(p[0], p[1]) for p in point_tuples]
for p in points:
    print(p, is_on_segment(p, a, b))