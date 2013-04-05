"""
======================
Watershed segmentation
======================

The watershed is a classical algorithm used for **segmentation**, that
is, for separating different objects in an image.

Starting from user-defined markers, the watershed algorithm treats
pixels values as a local topography (elevation). The algorithm floods
basins from the markers, until basins attributed to different markers
meet on watershed lines.  In many cases, markers are chosen as local
minima of the image, from which basins are flooded.

In the example below, two overlapping circles are to be separated. To
do so, one computes an image that is the distance to the
background. The maxima of this distance (i.e., the minima of the
opposite of the distance) are chosen as markers, and the flooding of
basins from such markers separates the two circles along a watershed
line.

See Wikipedia_ for more details on the algorithm.

.. _Wikipedia: http://en.wikipedia.org/wiki/Watershed_(image_processing)

"""
import skimage
import numpy as np
from skimage import transform
from skimage import io
import matplotlib.pyplot as plt
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from skimage import morphology
from skimage import color
from skimage import img_as_ubyte
from skimage import filter

image = img_as_ubyte(color.rgb2gray(io.imread('haai1.jpg')))
image = transform.resize(image, (460, 680))

markers = morphology.label(peak_local_max(image, indices=False))

edges = filter.sobel(image)
labels = watershed(edges, markers, mask=image)

fig, axes = plt.subplots(ncols=3, figsize=(8, 2.7))
ax0, ax1, ax2 = axes

ax0.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
ax1.imshow(markers, cmap=plt.cm.jet, interpolation='nearest')
ax2.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')

for ax in axes:
    ax.axis('off')

plt.subplots_adjust(hspace=0.01, wspace=0.01, top=1, bottom=0, left=0,
                    right=1)
plt.show()
