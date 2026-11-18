import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image_processing/image_arth/Screenshot 2026-11-04 093252.png')
img1 = cv2.imread('image_processing/image_arth/Screenshot 2026-11-04 093252.png')
img2 = cv2.imread('image_processing/image_arth/Screenshot 2026-11-04 093252.png')
img_add = cv2.add(img1, img2)
img_sub = cv2.subtract(img1, img2)
img_mul = cv2.multiply(img1, img2)
img_div = cv2.divide(img1, img2)
results = [
 ("Original Image", img),
 ("Addition: cv2.add()", img_add),
 ("Subtraction: cv2.subtract()", img_sub),
 ("Multiplication: cv2.multiply()", img_mul),
 ("Division: cv2.divide()", img_div),
]
plt.figure(figsize=(15, 10))
for k, (title, im) in enumerate(results, start=1):
 plt.subplot(2, 3, k)
 plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
 plt.title(title)
 plt.axis("off")
plt.tight_layout()
plt.show() 
