"""
2D multivariate spline over a triangulated grid (Delaunay + Clough-Tocher).

Clough-Tocher is a C1-continuous piecewise-cubic interpolant: each Delaunay
triangle is split into 3 sub-triangles with cubic Bezier patches, with
gradients estimated from the data so adjacent triangles join smoothly.
"""
import numpy as np
import matplotlib          # remove this line to get an interactive window
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from scipy.spatial import Delaunay
from scipy.interpolate import CloughTocher2DInterpolator

# ---------------- data (angle [deg], x2, value) ----------------
data = np.array([
    [ 0, 0.3, -0.0010],
    [ 0, 0.6, -0.0012],
    [ 0, 0.9, -0.0015],
    [10, 0.3, -0.0021],
    [10, 0.6, -0.0024],
    [10, 0.9, -0.0028],
    [20, 0.3, -0.0030],
    [20, 0.6, -0.0034],
    [20, 0.9, -0.0039],
])
pts, z = data[:, :2], data[:, 2]

# ---------------- triangulation + spline ----------------
tri = Delaunay(pts)
spline = CloughTocher2DInterpolator(tri, z)

# evaluate on a fine grid
A, B = np.meshgrid(np.linspace(0, 20, 120), np.linspace(0.3, 0.9, 120))
Z = spline(A, B)

# example query
print("spline(15 deg, 0.45) =", float(spline(15, 0.45)))

# ---------------- 3D visualization ----------------
fig = plt.figure(figsize=(13, 6))

# (left) smooth spline surface + data points + triangle edges on the data
ax = fig.add_subplot(1, 2, 1, projection="3d")
surf = ax.plot_surface(A, B, Z, cmap="viridis", alpha=0.85, linewidth=0, antialiased=True)
ax.scatter(pts[:, 0], pts[:, 1], z, c="red", s=50, depthshade=False, label="data")
ax.plot_trisurf(mtri.Triangulation(pts[:, 0], pts[:, 1], tri.simplices), z,
                color="none", edgecolor="k", linewidth=0.8)
ax.set_xlabel("Angle (deg)"); ax.set_ylabel("Parameter"); ax.set_zlabel("Value")
ax.set_title("Clough-Tocher C1 spline surface")
ax.view_init(elev=25, azim=-130)
ax.legend()
fig.colorbar(surf, ax=ax, shrink=0.6, pad=0.1)

# (right) the underlying linear triangle mesh for comparison
ax2 = fig.add_subplot(1, 2, 2, projection="3d")
ax2.plot_trisurf(mtri.Triangulation(pts[:, 0], pts[:, 1], tri.simplices), z,
                 cmap="viridis", edgecolor="k", linewidth=0.8)
ax2.scatter(pts[:, 0], pts[:, 1], z, c="red", s=50, depthshade=False)
ax2.set_xlabel("Angle (deg)"); ax2.set_ylabel("Parameter"); ax2.set_zlabel("Value")
ax2.set_title("Delaunay triangles (linear)")
ax2.view_init(elev=25, azim=-130)

plt.tight_layout()
plt.savefig("spline_triangles.png", dpi=150)
plt.show()