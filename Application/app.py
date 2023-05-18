from flask import Flask, render_template, request
import numpy as np
#import cv2
#import tensorflow as tf
#import keras
#from keras.models import load_model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/image_upload", methods = ['GET', 'POST'])
def image_upload():

    file_name = []
    temp_list = []

    image1 = request.files['image1']
    image1.save('static/images/'+image1.filename)

    temp_list.append(image1.filename)

    image_url = "static/images/" + image1.filename
    
    temp_list.append(image_url)
    
    file_name.append(temp_list)
    temp_list = []
    
    # image2 = request.files['image2']
    # image2.save('static/images/'+image2.filename)
    ## image2_url = "static/images/" + image2.filename
    # file_name.append(image2.filename)
    
    # image3 = request.files['image3']
    # image3.save('static/images/'+image3.filename)
    # file_name.append(image3.filename)

    # image4 = request.files['image4']
    # image4.save('static/images/'+image4.filename)
    # file_name.append(image4.filename)
    
    return render_template('output.html', image_file_names = file_name)

if __name__ == '__main__':
	app.run(debug=True)