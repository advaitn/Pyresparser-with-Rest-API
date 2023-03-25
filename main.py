import os
import urllib.request
from config import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import random
from datetime import date

# Resume Scrapper
from pyresparser import ResumeParser
import nltk
nltk.download('stopwords')



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/parse', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename) 
		random_number = str(random.randint(100000,999999)) + '_'
		today = date.today()
		d1 = today.strftime("%d%m%Y") + '_'
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], d1 + str(random_number) + filename))
		data = ResumeParser(os.path.join(app.config['UPLOAD_FOLDER'], d1 + str(random_number) + filename)).get_extracted_data()
		resp = jsonify({'message' : 'File successfully uploaded', 'data' : data})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp

if __name__ == "__main__":
    app.run(debug=True)