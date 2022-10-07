# Тепловая карта

import numpy as np
import numpy.random
import matplotlib.pyplot as plt

# Create data
temperature = np.random.randn(4096)
anger = np.random.randn(4096)

# Create heatmap
heatmap, xedges, yedges = np.histogram2d(temperature, anger, bins=(64,64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Plot heatmap
plt.clf()
plt.ylabel('Anger')
plt.xlabel('Temp')
plt.imshow(heatmap, extent=extent)
plt.show()
