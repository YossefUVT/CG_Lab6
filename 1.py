import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay, delaunay_plot_2d

points = [(3, 5), (6, 6), (6, 4), (9, 5), (9, 7)]

vor = Voronoi(points)
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

voronoi_plot_2d(vor, ax=ax[0])
ax[0].set_title("Voronoi Diagram")

tri = Delaunay(points)
delaunay_plot_2d(tri, ax=ax[1])
ax[1].set_title("Delaunay Triangulation")

plt.show()