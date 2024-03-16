from flask import Flask, request, send_from_directory, jsonify, render_template
import cv2
import os
import numpy as np
from color_grading import process_image_function, color_coordinates

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

MAX_FILE_AGE_DAYS = 1
MAX_FILES_TO_KEEP = 1

def cleanup_files(folder):
    files = os.listdir(folder)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    files_to_delete = files[:-MAX_FILES_TO_KEEP] if len(files) > MAX_FILES_TO_KEEP else []
    for file_name in files_to_delete:
        file_path = os.path.join(folder, file_name)
        os.remove(file_path)

def delete_old_files():
    cleanup_files(app.config['UPLOAD_FOLDER'])
    cleanup_files(app.config['PROCESSED_FOLDER'])


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    # Delete old files
    delete_old_files()
    
    if 'image' in request.files:
        # Get uploaded image
        file = request.files['image']
        #get file name from file
        file_name = file.filename
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        
        # Save image path to a text file
        with open('image_path.txt', 'w') as f:
            f.write(image_path)

        processed_image_path = os.path.join(app.config['PROCESSED_FOLDER'], file_name)
        file.save(image_path)
        image = cv2.imread(image_path)
    else:
        # Get processed image if no new image is uploaded
        processed_image_filename = request.form['processedImageFilename']
        processed_image_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_image_filename)
        image = cv2.imread(processed_image_path)
    
    # Get color coordinates from uploads folder ONLY
    color = request.form['color']
    with open('image_path.txt', 'r') as f:
        temp_image_path = f.read().strip()
    mask_image = cv2.imread(temp_image_path)
    color_ranges = color_coordinates(mask_image, color)

    percentage = int(request.form['percentage'])

    # Process image
    processed_image = process_image_function(image, color_ranges, percentage)

    # Save processed image
    cv2.imwrite(processed_image_path, processed_image)
    

    return jsonify({'imagePath': processed_image_path})

@app.route('/processed/<file_name>')
def processed_image(file_name):
    return send_from_directory(app.config['PROCESSED_FOLDER'], file_name)

if __name__ == '__main__':
    app.run(debug=True)
