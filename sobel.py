from skimage import io, filter, color
from skimage.filter import sobel
import matplotlib.pyplot as plt

A = color.rgb2gray(io.imread('haai1.jpg', plugin='pil'))
AA = sobel(A)

f, (ax0, ax1) = plt.subplots(1, 2)
plt.tight_layout()

ax0.imshow(A, cmap=plt.cm.gray)
ax0.set_title('Input image')

ax1.imshow(200*AA, cmap=plt.cm.gray)
ax1.set_title('Sobel operator applied')

plt.show()
