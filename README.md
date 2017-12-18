# Face Detection in Video Feed using OpenCV with Python

This Python script processes the video captured from the webcam and continuously detects any faces that might be present in it. In case of more than one face, it detects all the faces in the frame. It can also detect faces in any video file that can be read using OpenCV. 

The detection of faces is done using the Cascade Classifiers (Haar Frontal Face Classifier) and the classifier XML file must be available in the directory for the detection to take place. 

If you wish to detect faces in images, the logic remains mostly the same and you do away with the video capture and display portions of the code. The still photo face detection code has also been included. 

Application - Can be used as a base for several events that get triggered by the presence of a face in the aperture, e.g, snapping a photo every time there's a face in the frame etc. Since it continuously monitors webcam feed, you can also use it for applications where you wish to put your device to sleep/low power mode and fire it up when a face is detected in the camera frame.

The code has extensive comments explaining most of the logic and the use of various libraries and functions. 

Non-native dependencies - OpenCV

`pip install opencv-python`

Python version 3.5 and above (might work for lower versions of Python 3, not tested)
