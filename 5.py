from functools import cmp_to_key
import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

def analyze_triangulation_and_voronoi(points, plot=False):
    triangulation = Delaunay(points)

    num_triangles = len(triangulation.simplices)
    num_edges = len(triangulation.convex_hull) + len(triangulation.simplices) * 3 // 2

    return num_triangles, num_edges

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

m1 = [(2,2), (2,3), (3,4), (4,3), (3,3), (3,2)]
m2 = [(9,3), (10,3), (8,2), (9,2), (7,2), (8,3), (7,3)]

points_M1 = [Point(p[0], p[1]) for p in m1]
points_M2 = [Point(p[0], p[1]) for p in m2]
n1 = len(points_M1)
n2 = len(points_M2)
hull1 = convexHull(points_M1, n1)
hull2 = convexHull(points_M2, n2)
triangles1, edges1 = analyze_triangulation_and_voronoi(m1)
triangles2, edges2 = analyze_triangulation_and_voronoi(m2)

print("M1 | Triangles: ", triangles1, " Edges: ", len(edges1), " Half-Lines: ", len(hull1))
print("M2 | Triangles: ", triangles2, " Edges: ", len(edges2), " Half-Lines: ", len(hull2))