import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a blank image
image = np.zeros((300,300,3), dtype=np.uint8)
resized_image = image  # For simplicity, using same variable name as in original code

# cv2.rectangle parameters:
# 1. Image: The image to draw on
# 2. Start point: Top-left corner coordinates (x=50, y=50)
# 3. End point: Bottom-right corner coordinates (x=150, y=150)
# 4. Color: BGR format (0,0,255) = Red
# 5. Thickness: 5 pixels
cv2.rectangle(resized_image,(50,50),(150,150),(0,0,255),5)

# cv2.putText parameters:
# 1. Image: The image to draw on
# 2. Text: The string to be written
# 3. Position: Starting position of text (x=50, y=50)
# 4. Font: Font type (FONT_HERSHEY_SIMPLEX)
# 5. Font scale: Size of text (1)
# 6. Color: BGR format (0,0,255) = Red
# 7. Thickness: 2 pixels
cv2.putText(resized_image,"You didn't have to do it",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

# cv2.circle parameters:
# 1. Image: The image to draw on
# 2. Center: Center coordinates of circle (x=100, y=100)
# 3. Radius: 50 pixels
# 4. Color: BGR format (0,255,0) = Green
# 5. Thickness: 5 pixels (use -1 for filled circle)
cv2.circle(resized_image,(100,100),50,(0,255,0),5)

# Convert from BGR to RGB for proper color display in matplotlib
# Parameters for cv2.cvtColor:
# 1. src: Source image
# 2. code: Color conversion code (BGR to RGB)
plt.imshow(cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Parameters for cv2.imwrite:
# 1. Filename: Name of the output file "output_image.jpg"
# 2. Image: The image to be saved
cv2.imwrite("output_image.jpg",resized_image) 