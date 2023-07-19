import sys
sys.path.append("../")

import cv2
from detection.face_matching import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


def match_with_database(img, database):
    # Detect faces in the frame
    faces = detect_faces(img)

    for face in faces:
        try:
            # Align the face
            aligned_face = align_face(img, face)

            # Extract features from the face
            embedding = extract_features(aligned_face)

            embedding = embedding[0]["embedding"]

            # Match the face to a face in the database
            match = match_face(embedding, database)

            if match is not None:
                print(f"Match found: {match}")
            else:
                print("No match found")
        except:
            print("No face detected")
        # break # TODO: remove this line to detect all faces in the frame

    # Draw the rectangle around each face
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
        print("Face detected")

    # Display the frame
    cv2.imshow("Detected Faces", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cred = credentials.Certificate("../database/serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://face-recognition-486cb-default-rtdb.firebaseio.com/",
        "storageBucket": "face-recognition-486cb.appspot.com",
    },
)

# Information to database
ref = db.reference("Students")
# Obtain the last studentId number from the database
number_student = len(ref.get())
print("There are", (number_student - 1), "students in the database")

database = {}
for i in range(1, number_student):
    studentInfo = db.reference(f"Students/{i}").get()
    studentName = studentInfo["name"]
    studentEmbedding = studentInfo["embeddings"]
    database[studentName] = studentEmbedding

# print('Database:',database)
camera_or_image = input("Enter (1) if you have camera\nEnter (2) if you have image: ")

if camera_or_image == "1":
    # define a video capture object
    vid = cv2.VideoCapture(0)
    while True:
        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Add beatiful text to the frame to say save the image with 's' button
        cv2.putText(
            frame,
            "Press 's' to save the image",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
            cv2.LINE_AA,
        )

        # Display the resulting frame
        cv2.imshow("frame", frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    faces = match_with_database(frame, database)


elif camera_or_image == "2":
    # Read the image, TODO: this will come from the webcam later
    img = cv2.imread("../examples/face1.png")
    faces = match_with_database(img, database)
