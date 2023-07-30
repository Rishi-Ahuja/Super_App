from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('Images/numbers/0.9.png')
iar = np.array(i)
print(iar)
print(iar.shape)
print(iar.ndim)
plt.imshow(iar)
plt.show()
