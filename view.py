from app import app
import os
import urllib.request
from flask import Flask, flash, request, redirect, render_template, send_from_directory, current_app, send_file, jsonify
from werkzeug.utils import secure_filename

import csv


ALLOWED_EXTENSIONS = ['csv']
app.secret_key = "secret key"


def file_info(file_object):
	file = open(os.path.join('./upload', file_object))
	context = list(csv.reader(file))
	return len(context)

@app.route('/process', methods=['POST'])		
def process():
	filelist = []
	file_info_list = []
	for filename in os.listdir('./upload'):
		file_info_list.append(file_info(filename))
		filelist.append(filename)
	return render_template('process.html', filelist=filelist, file_info_list=file_info_list)


@app.route('/process/<path:file>')
def process_file(file):
	file_csv_read = open(os.path.join('./upload', file))
	context = list(csv.reader(file_csv_read))
	
	for line in context:
		line[0] = line[0].swapcase()
		print(line[0])
				
	new_filename = 'new' + file
	file_csv_write = os.path.join('./download', new_filename)
	with open(file_csv_write, 'w') as f_object:
		writer = csv.writer(f_object)
		for row in context:
			writer.writerow(row)

	return redirect('/')


@app.route('/')
def upload_form():
	return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:		#check for valid filename/extension
			filename = secure_filename(file.filename)
			file.save(os.path.join('./upload', filename))
			flash('File was successfully uploaded. Thank you.')
			return redirect('/')
		else:
			flash('Allowed file type is: csv')
			return redirect(request.url)


@app.route("/storage", methods=["GET", "POST"])
def get_file():
	print(os.listdir('./download'))
	filelist = []
	for filename in os.listdir('./download'):
		filelist.append(filename)
	return render_template('download.html', filelist=filelist)