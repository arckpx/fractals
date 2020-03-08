import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os

# Mandelbrot Set = {all convergent c} where z(n+1) = z(n) + c and z(0) = 0
# Julia island for c = complex(-0.79, 0.15) is at xmin, xmax, ymin, ymax = -0.825, -0.805, 0.190, 0.210

# Config
nx, ny = 1500, 1500  # number of pixels
xmin, xmax, ymin, ymax = -2, 0.5, -1.25, 1.25  # ranges
abs_max, count_max = 2, 200  # divergence limits

# Generate
mandelbrot = np.zeros((nx, ny))  # empty image
x_array = np.linspace(xmin, xmax, num=nx)
y_array = np.linspace(ymin, ymax, num=ny)
for ix in range(nx):
    for iy in range(ny):
        z = complex(0, 0)  # initialise z
        c = complex(x_array[ix], y_array[iy])
        count = 0
        while abs(z) < abs_max and count < count_max:  # loop
            z = z ** 2 + c
            count += 1
        mandelbrot[ix, iy] = count / count_max  # colour assignment
mandelbrot = np.flipud(mandelbrot.transpose())  # Argand diagram orientation

# Save
directory = './images'
if not os.path.exists(directory):
    os.makedirs(directory)
plt.imsave(os.path.join(directory, 'mandelbrot.png'), mandelbrot, cmap=cm.CMRmap)

# Plot
plt.imshow(mandelbrot, extent=[xmin, xmax, ymin, ymax], cmap=cm.CMRmap)
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
