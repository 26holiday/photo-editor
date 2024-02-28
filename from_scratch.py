import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk

SHIFT_FOR_RED = 50
SHIFT_FOR_BLUE = 50
SHIFT_FOR_GREEN = 50

# Prompt the user to enter the image file path
image_path = input("Enter the image file path: ")
def fit_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Check if the image was successfully loaded
    if image is not None:
        # Display the image
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to load the image.")
    return image

image = fit_image(image_path)

def change_hue(image, delta_hue):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Shift the hue channel
    hsv[:, :, 0] = (hsv[:, :, 0] + delta_hue) % 180
    
    # Convert HSV back to BGR
    modified_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return modified_image

# Use the function
updated_image = change_hue(image, 50)


def get_bgr_matrix(image_path):
    # Read the image
    # image = cv2.imread(image_path)
    image = image_path
    # Initialize an empty 2D list
    bgr_matrix = []

    # Iterate over each pixel in the image
    for i in range(image.shape[0]):
        row = []
        for j in range(image.shape[1]):
            # Append the BGR value of the pixel to the row
            row.append(image[i, j])
        # Append the row to the matrix
        bgr_matrix.append(row)
        image_array = np.array(bgr_matrix, dtype=np.uint8)
    return image_array

# Use the function
# image_array = get_bgr_matrix(image)

# print(bgr_matrix)
# print(image_array)

def get_pixel_coordinates_by_color(image, lower_color,upper_color):
    # Convert the color to a numpy array
    mask = cv2.inRange(image,lower_color,upper_color)
    # Find the coordinates of the pixels with the specified color
    coordinates = np.argwhere(mask == 255)
    return coordinates

# Define lower and upper bounds for colors in BGR color space

#RED
lower_red = np.array([0, 0, 70])
upper_red = np.array([100, 75, 255])

#BLUE
lower_blue = np.array([50, 0, 0])
upper_blue = np.array([255, 125, 100])

#GREEN
lower_green = np.array([0, 40, 0])
upper_green = np.array([100, 255, 100])

# red=get_pixel_coordinates_by_color(image, lower_red, upper_red)
# red = np.array(red)

# blue=get_pixel_coordinates_by_color(image, lower_blue, upper_blue)
# blue = np.array(blue)

# green = get_pixel_coordinates_by_color(image, lower_green, upper_green)
# green = np.array(green)

def shift_red_to_orange(image, red, shift):
    # Create a copy of the input image
    shifted_image = np.copy(image)
    # Iterate over the coordinates of the red pixels
    for coordinate in red:
        i, j = coordinate[0], coordinate[1]
        green_shift = image[i,j,1]
        green_shift += min(125,(image[i,j,2]/2)*(shift/100))
        shifted_image[i,j,1] = green_shift
    print(shifted_image[0,0,1])
    shifted_image = np.clip(shifted_image, 0, 255)
    return shifted_image

def shift_blue_to_green(image, blue, shift):
    # Create a copy of the input image
    shifted_image = np.copy(image)
    # Iterate over the coordinates of the red pixels
    for coordinate in blue:
        i, j = coordinate[0], coordinate[1]
        green_shift = image[i,j,1]
        temp_blue = image[i,j,0]
        green_shift += (temp_blue-green_shift)*(shift/100)
        shifted_image[i,j,1] = green_shift
    print(shifted_image[0,0,1])
    shifted_image = np.clip(shifted_image, 0, 255)
    return shifted_image

# shift green pixels to yellow
def shift_green_to_yellow(image, green, shift):
    # Create a copy of the input image
    shifted_image = np.copy(image)
    # Iterate over the coordinates of the red pixels
    for coordinate in green:
        i, j = coordinate[0], coordinate[1]
        red_shift = image[i,j,2]
        temp_green = image[i,j,1]
        red_shift += (temp_green-red_shift)*(shift/100)
        shifted_image[i,j,2] = red_shift
    print(shifted_image[0,0,2])
    shifted_image = np.clip(shifted_image, 0, 255)
    return shifted_image
# image_array =  shift_green_to_yellow(image_array, green, SHIFT_FOR_GREEN)
# image_array =  shift_red_to_orange(image_array, red, SHIFT_FOR_RED)
# image_array =  shift_blue_to_green(image_array, blue, SHIFT_FOR_BLUE)

# Write the array back to an image file
cv2.imshow('BGR Image', updated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output_image.jpg', updated_image)