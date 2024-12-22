import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay, delaunay_plot_2d

extended_points = [(5, 1), (7, -1), (9, -1), (7, 3), (11, 1), (9, 3), (8, -4), (8, 6)]

vor = Voronoi(extended_points)
voronoi_plot_2d(vor)
plt.title("Voronoi Diagram with A7 and A8")
plt.show()