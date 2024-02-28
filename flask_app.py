# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import numpy as np
# import cv2
# from color_grading import fit_image, get_bgr_matrix, get_pixel_coordinates_by_color, shift_blue_to_green, shift_green_to_yellow, shift_red_to_orange

# app = Flask(__name__)
# CORS(app)

# @app.route('/', methods=['POST'])
# def process_image():
#     data = request.json
#     # Extract data from the request
#     image_address = data.get('image_address')
#     red_shift = data.get('red_shift')
#     blue_shift = data.get('blue_shift')
#     green_shift = data.get('green_shift')

#     # Load the image
#     image = cv2.imread(image_address)
#     if image is None:
#         return jsonify({'status': 'error', 'message': 'Failed to load the image'})

#     # Get the BGR matrix
#     image_array = get_bgr_matrix(image)

#     # Get the pixel coordinates for each color
#     # RED
#     lower_red = np.array([0, 0, 70])
#     upper_red = np.array([100, 75, 255])

#     # BLUE
#     lower_blue = np.array([50, 0, 0])
#     upper_blue = np.array([255, 125, 100])

#     # GREEN
#     lower_green = np.array([0, 40, 0])
#     upper_green = np.array([100, 255, 100])

#     red = get_pixel_coordinates_by_color(image, lower_red, upper_red)
#     red = np.array(red)

#     blue = get_pixel_coordinates_by_color(image, lower_blue, upper_blue)
#     blue = np.array(blue)

#     green = get_pixel_coordinates_by_color(image, lower_green, upper_green)
#     green = np.array(green)

#     # Shift the pixels of each color
#     image_array = shift_red_to_orange(image_array, red, red_shift)
#     image_array = shift_blue_to_green(image_array, blue, blue_shift)
#     image_array = shift_green_to_yellow(image_array, green, green_shift)
#     cv2.imshow('BGR Image', image_array)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     # Convert image array to bytes
#     _, processed_image = cv2.imencode('.jpg', image_array)
#     processed_image_bytes = processed_image.tobytes()

#     # Create a response
#     response = {'status': 'success', 'message': 'Image processed successfully', 'processed_image': processed_image_bytes}
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)
