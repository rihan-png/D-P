# Image transformation
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('image_processing/image_transformation_neg_log.py/certificate.jpg') # Display the original image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
# Convert image to negative
negative_img = cv2.bitwise_not(img)
plt.imshow(cv2.cvtColor(negative_img, cv2.COLOR_BGR2RGB))
plt.title('Negative Image')
plt.show()
# Apply logarithmic transformation
c = 255 / np.log(256)  # Scaling constant
#c=1
log_img = c * np.log(1 + img)
log_img = np.float32(log_img)
plt.imshow(cv2.cvtColor(log_img, cv2.COLOR_BGR2RGB))
plt.title('Logarithmic Transformed Image')
plt.show()
# convert image to square root transformation
sqrt_img = np.sqrt(img)
sqrt_img = np.float32(sqrt_img)

plt.imshow(cv2.cvtColor(sqrt_img, cv2.COLOR_BGR2RGB))
plt.title('Square Root Transformed Image')
plt.show()
# Apply power-law (gamma) transformation
gamma = 10
gamma_img = np.power(img, gamma)
gamma_img = np.float32(gamma_img)
plt.imshow(cv2.cvtColor(gamma_img, cv2.COLOR_BGR2RGB))
plt.title('Power-Law (Gamma) Transformed Image')
plt.show()
