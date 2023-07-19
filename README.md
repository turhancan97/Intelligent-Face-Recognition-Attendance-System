# Face Recognition Attendance System

This project is a comprehensive attendance system that leverages the power of face recognition to identify individuals and mark their attendance. Built with Python, Flask, OpenCV, and Firebase, the system provides an efficient and automated solution to track attendance in various settings such as universities or workplaces. 

The system allows users to upload their image to the database, which is then used to recognize their face during attendance checks. The recognized faces are matched with the database, and the attendance is updated in real-time. The system also includes a secure login feature for teachers to view the attendance records. 

This project is an excellent example of how computer vision and machine learning can be used to automate traditional processes, making them more efficient and accurate.

## Table of Contents

- [Face Recognition Attendance System](#face-recognition-attendance-system)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Dependencies](#dependencies)
  - [Contribution](#contribution)
  - [Future Improvements](#future-improvements)
  - [License](#license)

## Introduction

In traditional attendance systems, the process of marking attendance is often manual, time-consuming, and prone to errors. With the advent of machine learning and computer vision, we now have the tools to automate this process and make it more efficient and accurate.

Our Face Recognition Attendance System is designed to leverage these technologies to provide a seamless and automated attendance tracking solution. The system uses face recognition technology to identify individuals and mark their attendance. This process eliminates the need for manual entry and reduces the chances of errors or fraudulent entries.

The system is built using Python, Flask, OpenCV, and Firebase. Python and Flask provide the backend functionality, OpenCV is used for face detection and recognition, and Firebase is used as the database to store user information and attendance records.

The system also includes a secure login feature for teachers, allowing them to view the attendance records. This feature ensures that only authorized individuals have access to the attendance data.

Whether you're a university looking to streamline your attendance tracking process or a business looking to automate your employee check-in system, our Face Recognition Attendance System provides a robust and efficient solution.

## Features

The **Face Recognition Attendance System** comes with a host of features designed to make attendance tracking as seamless and efficient as possible:

1. **Face Recognition**: The system uses advanced face recognition technology to identify individuals and mark their attendance. This eliminates the need for manual entry and ensures accuracy in attendance tracking.

2. **Real-Time Attendance Tracking**: The system tracks attendance in real-time. As soon as an individual is recognized by the system, their attendance is marked and updated in the database.

3. **Secure Teacher Login**: The system includes a secure login feature for teachers. This allows teachers to view the attendance records and ensures that only authorized individuals have access to this data.

4. **Multi-Class Support**: The system supports multiple classes. Students can be enrolled in multiple classes, and their attendance is tracked separately for each class.

5. **Database Integration**: The system is integrated with Firebase, a cloud-based NoSQL database. This allows for efficient storage and retrieval of user information and attendance records.

6. **Webcam Support**: The system supports webcam input for face recognition. This makes it easy to set up and use in a variety of settings.

7. **User-Friendly Interface**: The system features a user-friendly interface, making it easy for users to navigate and use the system.

8. **Open Source**: The system is open source. Developers are welcome to contribute and help improve the system.

## Installation

To get the Face Recognition Attendance System up and running on your local machine, follow these steps:

1. **Clone the Repository**: First, clone the repository to your local machine. You can do this by running the following command in your terminal:

   ```
   git clone https://github.com/turhancan97/Intelligent-Face-Recognition-Attendance-System.git
   ```


2. Create a virtual environment and activate it. You can do this by running the following commands in your terminal:

   python environment
   ```
   python -m venv your_env_name
   ```

   ```
   source your_env_name/bin/activate
   ```
   
   or 

   conda environment
   ```
   conda create -n your_env_name
   ```

   ```
   conda activate your_env_name
   ```

This will create a virtual environment and activate it. All the dependencies will be installed in this virtual environment. 

3. **Install Dependencies**: Navigate into the cloned project directory and install the necessary dependencies by running:

   ```
   pip install -r requirements.txt
   ```

   This command will install all the necessary libraries and packages listed in the `requirements.txt` file.

4. **Set Up Firebase**: The system uses Firebase for database operations. You need to set up a Firebase project and replace the Firebase configuration in the project with your own. You can follow the [Firebase setup guide](https://firebase.google.com/docs/web/setup) for instructions.

5. **Run the Application**: Once all the setup is complete, you can run the application by executing the following command in the terminal:

   ```
   python app.py
   ```

   This will start the Flask server and the application will be accessible at `http://localhost:5000`.

Please note that you need a webcam connected to your machine for the face recognition feature to work. If you are using a laptop, the built-in webcam will work fine.

## Usage

Once you have the Face Recognition Attendance System running, you can start using it by following these steps:

1. **Home Page**: Open your web browser and navigate to `http://localhost:5000`. This will take you to the home page of the application.

2. **Upload a New Face**: To add a new student to the system, click on the "Upload a new face as image" button. This will allow you to upload an image of the student's face. The image should be clear and the student's face should be visible. Also, you can capture the image from the camera by clicking on the "Capture a new face from camera" button.

3. **Add Student Information**: After uploading the image, you will be redirected to a page where you can enter the student's information. This includes the student's name, email, user type (student or teacher), classes they are enrolled in, and a password. Once you have entered all the information, click on the "Submit" button.

4. **Face Recognition**: Back on the home page, you can click on the "Recognize Face" button. This will start the face recognition process. The system will try to match the face in front of the webcam with the faces in the database.

5. **Class Selection**: If a match is found, you will be redirected to a page where you can select the class. The attendance for the selected class will be updated in the database.

6. **Teacher Login**: If you are a teacher, you can view the attendance by clicking on the "Teacher Login" button on the home page. You will be asked to enter a password. Once the correct password is entered, you will be redirected to the attendance page where you can see the list of students and their attendance.

Remember, the face recognition feature requires a webcam. If you are using a laptop, the built-in webcam will work fine. If you are using a desktop, you will need to connect a webcam to your machine.

## Dependencies

The Face Recognition Attendance System relies on several Python libraries to function correctly. Here is a list of the main dependencies:

- **Flask**: A lightweight web application framework. It is used to handle the web server side of the application.

- **OpenCV**: A library of programming functions mainly aimed at real-time computer vision. It is used to capture images from the webcam and perform face detection.

- **Firebase Admin**: A library for interacting with Firebase services. It is used to interact with the Firebase Realtime Database and Firebase Storage.

- **Werkzeug**: A comprehensive WSGI web application library. It is used to handle file uploads in Flask.

- **Pillow**: A Python Imaging Library adds image processing capabilities to your Python interpreter.

- **numpy**: A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

To install these dependencies, you can use pip, a package manager for Python. Simply run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This will install all the required packages. Make sure you are in the correct directory when you run this command (the directory should contain the `requirements.txt` file).

## Contribution

Contributions to the Face Recognition Attendance System are very welcome! If you have a feature request, bug report, or proposal for code refactoring, please feel free to open an issue or create a pull request.

Here are some ways you can contribute:

- **Improving the UI/UX**: The current interface is quite basic. If you have experience with front-end development and have some ideas on how to improve the user interface or user experience, your contributions would be greatly appreciated.

- **Adding new features**: If you have an idea for a new feature that would fit well with this project, feel free to suggest it by opening an issue. If you would like to implement it yourself, even better! Open a pull request with your changes and we will review it.

- **Reporting bugs**: If you encounter any bugs while using the system, please report them by opening an issue. Include as much information as possible about the bug and the circumstances under which it occurred.

- **Refactoring code**: As with any software project, there's always room for improvement in the codebase. If you see an opportunity to refactor some code to make it cleaner, more efficient, or more robust, we would be happy to review your proposal.

Before contributing, please make sure to check the existing issues and pull requests to avoid duplicating efforts. Also, when you open a pull request, make sure to include a clear and detailed description of the changes you have made.

Thank you for your interest in contributing to the Face Recognition Attendance System!

## Future Improvements

There are several areas where the system could be improved or expanded in the future:

- **Student ID Assignment**: Currently, the student ID is assigned as one more than the total number of images in the database. In the future, we plan to optimize this process by assigning missing student IDs (e.g., if the IDs are 1,2,3,4,[],6,7,8, the new image's ID will be 5).

- **User Interface Improvements**: We aim to enhance the aesthetic appeal of the interface to provide a more engaging user experience.

- **Database Image Addition**: As of now, an image is added to the database as soon as it is captured. We plan to modify this process so that an image is only added to the database after the corresponding information is entered.

- **Database Optimization**: We aim to optimize database operations to speed up the process by calling them only once.

- **Security Enhancements**: We plan to implement more secure methods for data handling and user authentication.

- **Student Login**: In the future, we plan to allow students to log into the system using their passwords.

- **Teacher Database**: We aim to create a separate database for teachers. When the 'Teacher Login' button is pressed, a username and password will be requested.

- **Teacher View**: Once logged in, teachers will be able to view student attendance based on the classes they teach.

- **Deployment**: Currently, the system is designed to run locally. In the future, we plan to deploy the system on a platform like Heroku, which would make it accessible from anywhere and not just on the local machine.

- **Improved error handling and user feedback**: While the system currently handles errors and provides feedback to the user, these aspects could be improved to make the system more robust and user-friendly.

- **Real-time updates**: At the moment, the attendance data is updated when the student logs in. In the future, we could implement real-time updates, so that the attendance data is updated instantly as soon as a student's face is recognized.

- **Integration with other systems**: The system could be integrated with other systems used in educational institutions, such as learning management systems or student information systems. This would allow for a more seamless experience for both students and teachers.

- **Additional Features**: There are many additional features that could be added to the system, such as support for multiple cameras, recognition of multiple faces at once, or the ability to handle different lighting conditions.

These are just a few ideas for future improvements. We are always open to new ideas and suggestions, so feel free to contribute!

## License

This project is licensed under the MIT License. This means you are free to use, modify, and distribute the project under the terms of this license. Please see the [LICENSE](LICENSE) file for more details. 

Please note that this project is provided "as is" without any warranty. The authors are not responsible for any damage or issues that may arise from using the project. Always check the code yourself before using it in a production environment.

**Project Outline:**
1. Project Introduction
2. System Design and Development
3. Testing and Evaluation
4. Deployment and User Training
5. Maintenance and Updates

**Detailed Project Plan:**

**Phase 1: Project Introduction**
Tasks:
- Define the project scope, objectives, and deliverables.
- Identify the project requirements and constraints.
- Set up a project timeline and milestones.

**Phase 2: System Design and Development**
Tasks:
- **Task 1: Design System Architecture**
  - Define the system components and their interactions.
  - Design the database schema for Firebase.
  - Design the user interface for the web application.

- **Task 2: Develop Face Recognition System**
  - Research and select appropriate face recognition algorithms.
  - Implement the face recognition system using Python and OpenCV.
  - Integrate the face recognition system with the Firebase database.

- **Task 3: Develop User Interface**
  - Implement the user interface for the web application.
  - Ensure the interface is user-friendly and intuitive.
  - Connect the user interface with the face recognition system and the Firebase database.

**Phase 3: Testing and Evaluation**
Tasks:
- **Task 1: Unit Testing**
  - Test each component of the system individually to ensure it functions as expected.

- **Task 2: Integration Testing**
  - Test the system as a whole to ensure all components work together seamlessly.

- **Task 3: User Acceptance Testing**
  - Have a small group of end-users test the system and provide feedback.

**Phase 4: Deployment and User Training**
Tasks:
- **Task 1: Deployment**
  - Deploy the system for use in the intended environment.

- **Task 2: User Training**
  - Conduct training sessions for users to ensure they understand how to use the system.

**Phase 5: Maintenance and Updates**
Tasks:
- **Task 1: System Maintenance**
  - Regularly monitor the system for any issues or bugs.

- **Task 2: System Updates**
  - Regularly update the system based on user feedback and technological advancements.

---

**Project Introduction**

1. **Project Overview**
   - Briefly describe the project, its objectives, and its expected outcomes. Explain the problem that the project aims to solve and how the proposed system, the 'Intelligent Face Recognition Attendance System', will address this problem.

2. **Project Scope**
   - Define the boundaries of the project. What will the project include and what will it not include? For example, the project will include the development of a face recognition system and a user interface, but it will not include the development of hardware components as it will utilize existing systems.

3. **Project Objectives**
   - Clearly state what the project aims to achieve. The main objective of this project is to develop an Intelligent Face Recognition Attendance System that uses digital images or video frames to automatically identify and verify the identification of an individual for attendance purposes.

4. **Project Deliverables**
   - List the tangible items or results that will be delivered to the client at the end of the project. This could include the face recognition system, the user interface, user manuals, etc.

5. **Project Requirements**
   - Identify the specific requirements that the project must meet. This could include technical requirements (e.g., the system must be able to accurately recognize faces in different lighting conditions), user requirements (e.g., the system must be user-friendly and easy to use), and legal requirements (e.g., the system must comply with data privacy laws).

6. **Project Constraints**
   - Identify any limitations or restrictions that could impact the project. This could include budget constraints, time constraints, resource constraints, etc.

7. **Project Timeline and Milestones**
   - Provide an estimated timeline for the project, including key milestones. The timeline should provide a high-level view of when each phase of the project (e.g., system design and development, testing and evaluation, deployment and user training, etc.) is expected to start and finish.

This section sets the foundation for the project and provides a clear understanding of what the project will entail. It's important to ensure that all stakeholders are on the same page regarding the project's scope, objectives, deliverables, requirements, constraints, and timeline.

---

**System Design and Development**

1. **System Architecture Design**
   - Define the system components and their interactions. This includes the face recognition system, the user interface, and the Firebase database. Create a diagram to visually represent the system architecture.

2. **Database Design**
   - Design the database schema for Firebase. This includes defining the data that will be stored (e.g., student information, attendance records, etc.) and how this data will be structured and related.

3. **User Interface Design**
   - Design the user interface for the web application. This includes defining the layout, colors, fonts, and images that will be used. The interface should be user-friendly and intuitive.

4. **Face Recognition System Development**
   - Research and select appropriate face recognition algorithms. This could include algorithms for face detection, feature extraction, and face matching.
   - Implement the face recognition system using Python and OpenCV. This includes writing the code to capture images or video frames, detect faces, extract features, and match faces.
   - Integrate the face recognition system with the Firebase database. This includes writing the code to store and retrieve data from the database.

5. **User Interface Development**
   - Implement the user interface for the web application. This includes writing the HTML, CSS, and JavaScript code to create the interface based on the design.
   - Connect the user interface with the face recognition system and the Firebase database. This includes writing the code to display data from the database on the interface and to send data from the interface to the database.

6. **System Integration**
   - Integrate all components of the system to ensure they work together seamlessly. This includes ensuring that the face recognition system, the user interface, and the Firebase database can communicate with each other effectively.

This section involves a lot of technical work and requires a good understanding of Python, OpenCV, Firebase, and web development. It's important to test each component as it's developed to catch any issues early and ensure that the final system functions as expected.