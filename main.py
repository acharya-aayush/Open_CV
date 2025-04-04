import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((300,300,3), dtype=np.uint8)

plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
#plt.axis('off')
plt.show()  

print("Imported")