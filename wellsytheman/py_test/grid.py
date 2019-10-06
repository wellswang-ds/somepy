from ease_grid import EASE2_grid
from itertools import chain
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


egrid = EASE2_grid(36000)
assert egrid.shape == (406, 964)
# these two attributes contain the longitude and latitude coordinate dimension
print(egrid.londim)
print(egrid.latdim)
# print(egrid)



def draw_map(m, scale=0.2):
    # draw a shaded-relief image
    m.shadedrelief(scale=scale)

    # lats and longs are returned as a dictionary
    # lats = m.drawparallels(np.linspace(-90, 90, 13))
    # lons = m.drawmeridians(np.linspace(-180, 180, 13))
    lats = m.drawparallels(np.array(egrid.latdim))
    lons = m.drawmeridians(np.array(egrid.londim))
    # print(lats)

    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)
    # print(lat_lines)

    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.4, color='blue')

fig = plt.figure(figsize=(8*2, 6*2), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
draw_map(m)
plt.show()
