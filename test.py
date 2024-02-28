import cv2
import numpy as np

# Read the image
image_path = input("Enter the image file path: ")
image = cv2.imread(image_path)

# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the color range in HSV
# Example: defining a range for blue color
hue_min = 90
saturation_min = 50
value_min = 50
hue_max = 130
saturation_max = 255
value_max = 255

red1_min = np.array([159, 50, 70])
red1_max = np.array([179, 255, 255])

# Red2
red2_min = np.array([0, 50, 70])
red2_max = np.array([9, 255, 255])


# Create a mask to isolate pixels within the specified color range
lower_color = np.array([hue_min, saturation_min, value_min])
upper_color = np.array([hue_max, saturation_max, value_max])
mask = cv2.inRange(hsv, red2_min, red2_max) + cv2.inRange(hsv, red1_min, red1_max)

# Find the coordinates of the pixels with the specified color
coordinates = np.argwhere(mask == 255)

# Print the coordinates (optional)
# print("Coordinates of pixels with the specified color:")
# for coord in coordinates:
#     print(coord)

# Visualize the mask
cv2.imshow('Mask', mask)

# Optionally, draw circles on the original image at the coordinates of pixels with the specified color
for coord in coordinates:
    cv2.circle(image, tuple(coord[::-1]), 3, (0, 255, 0), -1)  # Draw a green circle

# Display the image with marked pixels
cv2.imshow('Image with Marked Pixels', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
