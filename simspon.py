from Imagex import *
from ImageProcessing import *
from Clustering import *
from Blob import *
from pylab import figure

img=Imagex()
img.loadImage("coins.jpg")
binaryImage = rgb2gray(img)
binaryze(binaryImage,100)
labeled, blobs = labelClustering(binaryImage)
fig = figure()

h = img.imgShow()
ax = h.axes 

for b in range(0,len(blobs)):
    x = blobs[b]._xMin
    y = blobs[b]._yMin
    w = blobs[b]._width
    h = blobs[b]._height
    c = blobs[b]._color
    r = Rectangle((x,y),w, h, fill=False, edgecolor=c,linewidth=3)
    ax.add_patch(r)

fig.show() 