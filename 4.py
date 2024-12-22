from functools import cmp_to_key

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

p0 = Point(0, 0)

def nextToTop(S):
    return S[-2]

def distSq(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def compare(p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0:
        return -1 if distSq(p0, p2) >= distSq(p0, p1) else 1
    return -1 if o == 2 else 1

def convexHull(points, n):
    ymin = points[0].y
    min = 0
    for i in range(1, n):
        y = points[i].y
        if y < ymin or (ymin == y and points[i].x < points[min].x):
            ymin = points[i].y
            min = i

    points[0], points[min] = points[min], points[0]
    global p0
    p0 = points[0]
    points = sorted(points, key=cmp_to_key(compare))

    m = 1
    for i in range(1, n):
        while i < n - 1 and orientation(p0, points[i], points[i + 1]) == 0:
            i += 1
        points[m] = points[i]
        m += 1

    if m < 3:
        return []

    S = [points[0], points[1]]
    for i in range(2, m):
        while len(S) > 1 and orientation(nextToTop(S), S[-1], points[i]) == 1:
            S.pop()
        S.append(points[i])

    return [(p.x, p.y) for p in S]


points_A = [(1 + i, i - 1) for i in range(6)]
points_B = [(-i, i) for i in range(6)]
points_C = [(0, i) for i in range(6)]
total_points = points_A + points_B + points_C
points = [Point(p[0], p[1]) for p in total_points]
n = len(points)
hull = convexHull(points, n)

print(len(hull))