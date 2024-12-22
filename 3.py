def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def mst(points):
    edges = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i < j:
                edges.append((distance(p1, p2), i, j))
    edges.sort()

    parent = list(range(len(points)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    mst_length = 0
    for dis, u, v in edges:
        pu, pv = find(u), find(v)
        if pu != pv:
            mst_length += dis
            parent[pu] = pv
    return mst_length

points = [(1, 6), (1, 1), (-4, 7), (6, 7), (1, -1), (5, 3), (-2, 3)]
a_range = [i/10 for i in range(-100, 101, 1)]
min_length = None
min_a = None

for a in a_range:
    newPoints = points + [(a - 2, 3)]
    tree_length = mst(newPoints)

    if min_length == None:
        min_length = tree_length
        min_a = a
    else:
        if tree_length < min_length:
            min_length = tree_length
            min_a = a

print(min_a)