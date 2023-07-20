import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 6)
print('x = ' , x)
y = np.linspace(-4, 4, 6)
print('y = ', y)
X, Y = np.meshgrid(x, y)
print('X = ', X)
print('Y = ', Y)
U = X + Y
print('U = ', U)
V = Y - X
print('V = ', V)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V, color="C0", angles='xy', scale_units='xy', scale=5, width=.015)
ax.set(xlim=(-5, 5), ylim=(-5, 5))
plt.show()