from flask import Flask, render_template, request, redirect, url_for, Response
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
import io
from PIL import Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from detection.face_matching import * 

app = Flask(__name__, template_folder='template')

# Specify the directory to save uploaded images
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_info')
def add_info():
    return render_template('add_info.html')

@app.route('/upload', methods=['POST'])
def upload():
    global filename
    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    # Check if the file is one of the allowed types/extensions
    if file.filename == '':
        return 'No selected file', 400

    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # change the name of the file to the studentId
        # Information to database
        ref = db.reference('Students')
        # Obtain the last studentId number from the database
        studentId = len(ref.get())

        filename = f'{studentId}.png'

        # Move the file from the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Upload the file to the database
        val,err = upload_database(filename)

        if val:
            return err
        
        # Redirect the user to the uploaded_file route, which
        # will basically show on the browser the uploaded file
        return redirect(url_for('add_info'))

    return 'File upload failed', 400

def allowed_file(filename):
    # Put your allowed file types here
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Generate the URL of the image
    url = url_for('static', filename='images/' + filename)
    # Return an HTML string that includes an <img> tag
    return f'<h1>File uploaded successfully</h1><img src="{url}" alt="Uploaded image">'


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    global filename
    ret, frame = video.read()
    if ret:
        # Information to database
        ref = db.reference('Students')
        # Obtain the last studentId number from the database
        studentId = len(ref.get())

        # Save the image
        filename = f'{studentId}.png'
        # Save the frame as an image
        cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], filename), frame)

        # Upload the file to the database
        val,err = upload_database(filename)

        if val:
            return err
    # Redirect to the success page
    return redirect(url_for('add_info'))

@app.route('/success/<filename>')
def success(filename):
    # Generate the URL of the image
    url = url_for('static', filename='images/' + filename)
    # Return an HTML string that includes an <img> tag
    return f'<h1>{filename} image uploaded successfully to the database</h1><img src="{url}" alt="Uploaded image">'

@app.route('/submit_info', methods=['POST'])
def submit_info():
    # Get the form data
    name = request.form.get('name')
    email = request.form.get('email')
    userType = request.form.get('userType')
    password = request.form.get('password')

    # Get the last uploaded image
    studentId, _ = os.path.splitext(filename)
    fileName = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    data = cv2.imread(fileName)

    # Detect faces in the image
    faces = detect_faces(data)

    for face in faces:
        # Align the face
        aligned_face = align_face(data, face)

        # Extract features from the face
        embedding = extract_features(aligned_face)
        break

    # Add the information to the database
    ref = db.reference('Students')
    data = {
        str(studentId) : 
        {
        'name': name,
        'email': email,
        'userType': userType,
        'password': password,
        'embeddings': embedding[0]['embedding']
        }
    }
    
    for key, value in data.items():
        ref.child(key).set(value)

    return redirect(url_for('success', filename=filename))

def gen_frames():
    global video
    video = cv2.VideoCapture(0)
    while True:
        success, frame = video.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__ == '__main__':
    # Initialize Firebase
    cred = credentials.Certificate("database/serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://face-recognition-486cb-default-rtdb.firebaseio.com/',
        'storageBucket': 'face-recognition-486cb.appspot.com'
        })
    
    def upload_database(filename):
        valid = False
        # If the fileName exists in the database storage, then continue
        if storage.bucket().get_blob(filename):
            valid = True
            error =  f'<h1>{filename} already exists in the database</h1>'
        
        # First check if the name of the file is a number
        if not filename[:-4].isdigit():
            valid = True
            error = f'<h1>Please make sure that the name of the {filename} is a number</h1>'

        if not valid:
            # Image to database
            filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            bucket = storage.bucket()
            blob = bucket.blob(filename)
            blob.upload_from_filename(filename)
            error = None

        return valid, error

    app.run(debug=True)