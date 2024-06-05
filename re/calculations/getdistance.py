import cv2
import numpy as np

# Load the image
image = cv2.imread('tree_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment out the tree
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and find the contour with the maximum area
max_contour = max(contours, key=cv2.contourArea)

# Calculate the height of the tree in pixels
x, y, w, h = cv2.boundingRect(max_contour)
tree_height_in_pixels = h

# Focal length of the camera in pixels
focal_length = 1000  # Replace with the actual focal length of your camera

# Real-world height of the tree in inches
real_world_tree_height = 10  # Replace with the actual height of the tree

# Calculate the distance between the camera and the tree
distance = (real_world_tree_height * focal_length) / tree_height_in_pixels

print("Distance between the camera and the tree: ", distance, "inches")