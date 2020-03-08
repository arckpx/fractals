import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cv2
import os

# Julia Set = {all convergent z} where z(n+1) = z(n) + c and c is fixed

# Config
nx, ny = 200, 200  # number of pixels
xmin, xmax, ymin, ymax = -2, 2, -2, 2  # ranges
abs_max, count_max = 10, 50  # divergence limits

imagenum = 100  # number of images
t = np.linspace(0.89, 2 * np.pi + 0.89, num=imagenum)
r = np.sin(t) + 1.23

# Generate & Save
directory = './video'
if not os.path.exists(directory):
    os.makedirs(directory)

x_array = np.linspace(xmin, xmax, num=nx)
y_array = np.linspace(ymin, ymax, num=ny)
c_array = []
for i in range(imagenum):
    c = r[i] * np.exp(1j * t[i])
    c_array.append(c)
for ic in range(len(c_array)):
    julia = np.zeros((nx, ny))  # empty image
    for ix in range(nx):
        for iy in range(ny):
            z = complex(x_array[ix], y_array[iy])
            count = 0
            while abs(z) < abs_max and count < count_max:  # loop
                z = z ** 2 + c_array[ic]
                count += 1
                julia[ix, iy] = count / count_max  # colour assignment
    julia = np.flipud(julia.transpose())  # Argand diagram orientation

    filename = 'julia_{:04d}.png'.format(ic + 1)
    plt.imsave(os.path.join(directory, filename), julia, cmap=cm.CMRmap)

    print('Image {} of {} has been processed.'.format(ic + 1, imagenum))

# Make a video
images = [img for img in os.listdir(directory) if img.endswith(".png")]
height, width, layers = cv2.imread(os.path.join(directory, images[0])).shape
video = cv2.VideoWriter(os.path.join(directory, 'julia.avi'), 0, 10, (width, height))
for image in images:
    video.write(cv2.imread(os.path.join(directory, image)))
    os.remove(os.path.join(directory, image))
cv2.destroyAllWindows()
video.release()
