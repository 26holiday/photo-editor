import numpy as np
import cv2

# image_path = input("Enter the image file path: ")
def fit_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Check if the image was successfully loaded
    if image is not None:
        # Display the image
        cv2.imshow("Image", image)
    else:
        print("Failed to load the image.")
    return image

# image = fit_image(image_path)

def change_hue(image,coordinates, percentage):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    #split coordinates into x,y
    x = coordinates[:,0]
    y = coordinates[:,1]
    # Shift the hue channel
    delta_hue = (percentage / 100) * 25

    hsv[x, y, 0] = (hsv[x, y, 0] + delta_hue + 180) % 180
    
    # Convert HSV back to BGR
    modified_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return modified_image

def get_pixel_coordinates_by_color(image, lower_color,upper_color):
    #convert image to hsv
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Convert the color to a numpy array
    mask = cv2.inRange(image,lower_color,upper_color)
    # Find the coordinates of the pixels with the specified color
    coordinates = np.argwhere(mask == 255)
    return coordinates

def shift_color_range(min_values, max_values, percentage):
    delta = (percentage / 100) * 255
    min_values = np.clip(min_values + delta, 0, 255)
    max_values = np.clip(max_values + delta, 0, 255)
    return min_values, max_values

def color_coordinates(image, color):
    color_ranges = {
    'black': (np.array([0, 0, 0]), np.array([180, 255, 30])),
    'white': (np.array([0, 0, 231]), np.array([180, 18, 255])),
    'red1': (np.array([159, 50, 70]), np.array([179, 255, 255])),
    'red2': (np.array([0, 50, 70]), np.array([9, 255, 255])),
    'green': (np.array([36, 50, 70]), np.array([89, 255, 255])),
    'blue': (np.array([90, 50, 70]), np.array([128, 255, 255])),
    'yellow': (np.array([25, 50, 70]), np.array([35, 255, 255])),
    'purple': (np.array([129, 50, 70]), np.array([158, 255, 255])),
    'orange': (np.array([10, 50, 70]), np.array([24, 255, 255])),
    'gray': (np.array([0, 0, 40]), np.array([180, 18, 230])),
    'magenta': (np.array([129, 50, 70]), np.array([158, 255, 255])),
    'cyan': (np.array([90, 50, 70]), np.array([128, 255, 255]))
    }
    #condition to cheeck if color is red or not
    if color == 'red':
        red1_min, red1_max  = color_ranges['red1']
        red2_min, red2_max = color_ranges['red2']
        red1 = get_pixel_coordinates_by_color(image, red1_min, red1_max)
        red2 = get_pixel_coordinates_by_color(image, red2_min, red2_max)
        red = np.concatenate((red1, red2), axis=0)
        red = np.unique(red, axis=0)
        color_coordinates = red
    else:
        min_values, max_values = color_ranges[color]
        color_coordinates = get_pixel_coordinates_by_color(image, min_values, max_values)
    return color_coordinates

def process_image_function(image, color_coordinates, percentage):
    updated_image = change_hue(image,color_coordinates,percentage)
    print("skfjekjfsl rtk")
    return updated_image

#test the function
# image = cv2.imread('test2.jpg')
# color_ranges = color_coordinates(image, 'red')
# updated_image = process_image_function(image, color_ranges, 100)

# print(red)
# updated_image = process_image_function(image, 'red', 50)

# Write the array back to an image file
# cv2.imshow('BGR Image', updated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('output_image.jpg', updated_image)

