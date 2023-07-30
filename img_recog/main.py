import numpy as np
import matplotlib.pyplot as pl

x = np.linspace(1, 5, 6)
y = np.log(x)
pl.plot(x, y)
pl.xlabel('X Values')
pl.ylabel('Y Values')
pl.bar(x, y, width=0.5, color=['y', 'r', 'b', 'k', 'm', 'c'])
pl.show()
