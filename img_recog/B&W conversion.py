from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

i = Image.open('Images/backdrop.jpg')
iar = np.array(i)
print(iar.shape)
print(iar.ndim)
mp = []

for eachrow in iar:
    for eachpixel in eachrow:
        m = mean(eachpixel)
        mp.append(m)
mi = mean(mp)

for eachrow in iar:
    for eachpixel in eachrow:
        if mean(eachpixel) > mi:
            eachpixel[0] = 255
            eachpixel[1] = 255
            eachpixel[2] = 255
        else:
            eachpixel[0] = 0
            eachpixel[1] = 0
            eachpixel[2] = 0

plt.imshow(iar)
plt.show()
