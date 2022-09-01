import numpy
import matplotlib.pyplot as plt
import rasterio
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
from rasterio import plot
import os

image_file = "../"

# path of image file to be processed

with rasterio.open(image_file) as src:
    band_red = src.read(1)

with rasterio.open(image_file) as src:
    band_green = src.read(2)

with rasterio.open(image_file) as src:
    band_blue = src.read(3)

numpy.seterr(divide='ignore', invalid='ignore')

band_red = numpy.array(band_red)
band_green = numpy.array(band_green)
band_blue = numpy.array(band_blue)

VARI = (band_green.astype(int)-band_red.astype(int))/(band_green.astype(int) + band_red.astype(int) - band_blue.astype(int))

fig1, ax = plt.subplots(figsize=(12, 12))

ep.plot_bands(VARI,
              cmap='RdYlGn',
              scale=False,
              cbar=False,
              ax=ax,
              vmin=-1, vmax=1,
              title="VARI"
              )
plt.show()