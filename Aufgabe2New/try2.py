import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5]

X, Y = np.meshgrid(x, y)
Z = np.array([[1, 2, 2.5, 2.7, 2.8, 2.8, 2.7, 2.5, 2, 1],
              [1, 2, 2.5, 2.7, 2.8, 2.8, 2.7, 2.5, 2, 1],
              [1, 2, 2.5, 2.7, 2.8, 2.8, 2.7, 2.5, 2, 1],
              [1, 2, 2.5, 2.7, 2.8, 3.8, 2.7, 2.5, 3, 1],
              [1, 2, 2.5, 2.7, 2.8, 2.8, 2.7, 2.5, 2, 1]])





# 设置坐标轴标志
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.gca().set_box_aspect((10, 5, 5))


ax.plot_surface(X, Z, Y, color='orange')
plt.show()
