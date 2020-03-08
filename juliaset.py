import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os

# Julia Set = {all convergent z} where z(n+1) = z(n) + c and c is fixed

# Config
nx, ny = 500, 500  # number of pixels
xmin, xmax, ymin, ymax = -0.825, -0.805, 0.19, 0.21  # ranges
abs_max, count_max = 2, 200  # divergence limits

c = complex(-0.79, 0.15)

# Generate
julia = np.zeros((nx, ny))  # empty image
x_array = np.linspace(xmin, xmax, num=nx)
y_array = np.linspace(ymin, ymax, num=ny)
for ix in range(nx):
    for iy in range(ny):
        z = complex(x_array[ix], y_array[iy])
        count = 0
        while abs(z) < abs_max and count < count_max:  # loop
            z = z ** 2 + c
            count += 1
        julia[ix, iy] = count / count_max  # colour assignment
julia = np.flipud(julia.transpose())  # Argand diagram orientation

# Save
directory = './images'
if not os.path.exists(directory):
    os.makedirs(directory)
plt.imsave(os.path.join(directory, 'julia.png'), julia, cmap=cm.CMRmap)

# Plot
plt.imshow(julia, extent=[xmin, xmax, ymin, ymax], cmap=cm.CMRmap)
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()
