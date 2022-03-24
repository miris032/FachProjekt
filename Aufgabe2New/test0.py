import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from matplotlib.colors import LightSource
from matplotlib.ticker import LinearLocator
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# 窗口大小
fig = plt.figure(figsize=(12, 8))

# 坐标系在窗口中的位置
ax = fig.add_subplot(111, projection='3d')

X = np.arange(1, 1374, 1)
Y = np.arange(1, 442, 1)
X, Y = np.meshgrid(X, Y)
Z = pd.read_csv("../../../FachProjekt/Aufgabe2/OberflächentopographieDatei.txt", sep=' ', header=None).to_numpy()

# z轴范围
ax.set_zlim(-2, 2)

'''ax.set_xlim(0, 429)
ax.set_ylim(0, 292)'''

# 设置坐标轴标志
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")


print(Z.shape)




'''# create light source object.
ls = LightSource(azdeg=0, altdeg=650)
# shade data, creating an rgb array.
rgb = ls.shade(Z, plt.cm.RdYlBu)'''




# surf = ax.plot_surface(X, Y, Z, cmap=plt.get_cmap('copper'), antialiased=True) # cmap=cm.coolwarm,   , facecolors=rgb    ,rstride=1, cstride=1, linewidth=0
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0, linewidth=0.5, antialiased=True)
surf = ax.plot_wireframe(X, Y, Z, rstride=20, cstride=20, linewidth=0.5, color='black')
surf2 = surf


# ax.grid(False)
plt.gca().set_box_aspect((1, 411/1373, 1))

# 三种缩放
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([0.44, 1, 0.5, 0.5]))
# fig.subplots_adjust(bottom=-0.15, top=1.2)
# ax.auto_scale_xyz([0, 4000], [0, 1000], [0, 1])


'''
# 等高线影子
ax.contour(X, Y, Z, zdir='z', offset=-1, cmap=plt.get_cmap('coolwarm')) # rainbow
'''


'''
# 去掉坐标系
plt.axis('off')
plt.grid(visible=None)'''


if __name__ == '__main__':
    # plt.imshow()
    plt.axis('off')
    plt.show()
