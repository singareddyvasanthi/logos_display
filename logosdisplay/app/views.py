# Important imports
from app import app
from flask import request, render_template
import os
import cv2
import numpy as np
from PIL import Image

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

# Route to home page


@app.route("/", methods=["GET", "POST"])
def index():

    # Execute if request is get
    if request.method == "GET":
        return render_template("index.html")

    # Execute if reuqest is post
    if request.method == "POST":
        option = request.form['options']
        image_upload = request.files['image_upload']
        imagename = image_upload.filename
        image = Image.open(image_upload)
        image_logow = np.array(image.convert('RGB'))
        h_image, w_image, _ = image_logow.shape

        if option == 'logo_watermark':
            logo_upload = request.files['logo_upload']
            logoname = logo_upload.filename
            logo = Image.open(logo_upload)
            image.save(os.path.join(
                app.config['INITIAL_FILE_UPLOADS'], 'image.png'))
            full_filename = 'static/uploads/image.png'
            return render_template('index.html', full_filename=full_filename)

        else:
            text_mark = request.form['text_mark']
            image.save(os.path.join(
                app.config['INITIAL_FILE_UPLOADS'], 'image1.png'))
            full_filename = 'static/uploads/image1.png'
            return render_template('index.html', full_filename=full_filename)


# Main function
if __name__ == '__main__':
    app.run(debug=True)
