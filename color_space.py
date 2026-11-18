# Write Program to read and display image
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('image_processing/image_color/Screenshot_2026-08-21-10-45-18-37.jpg') # Read the image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert BGR to RGB and display
plt.show()

# Covert the image to grayscale
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray') # Display the grayscale image
plt.show()

# convert the image to black and white
ret, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
plt.imshow(bw, cmap='gray') # Display the black and white image
plt.show()

#Convert the image to HSV
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(hsv)
plt.show()
