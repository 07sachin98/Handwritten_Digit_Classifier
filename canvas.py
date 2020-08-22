from keras.models import load_model

from flask import Flask ,render_template,url_for,request

import numpy as numpy

#from scipy.misc import imsave, imread, imresize

from imageio import imsave, imread#, imresize

#for regular expressions, saves time dealing with string data
import re

#system level operations (like loading files)
import sys
#for reading operating system data
import os


app=Flask(__name__)

@app.route('/ui')
def UI():
    return render_template('canvas.html')

#convert raw image
def convertImage(imgData1):
	imgstr = re.search(r'base64,(.*)',imgData1).group(1)
	#print(imgstr)
	with open('output.png','wb') as output:
		output.write(imgstr.decode('base64'))


def preprocess_img():

	img_data=request.get_data()
	convertImage(img_data)

	#read the image into memory
	x = imread('output.png',mode='L')
	#compute a bit-wise inversion so black becomes white and vice versa
	#x = np.invert(x)
	#make it the right size
   #x = imresize(x,(28,28))
	#imshow(x)
	#convert to a 4D tensor to feed into our model
	x = x.reshape(1,28,28,1)

	return x

@app.route('/predict',methods=['GET','POST'])
def predict():

	mnist_model=load_model("model.h5")

	#model.summary()

	if request.method == 'POST':
		image_out=preprocess_img()
		message = request.form['canvas']
		data = [message]
		img_out=np.array(preprocess(data))
		my_prediction = mnist_model.predict_classes(img_out)
		return render_template('canvas.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
