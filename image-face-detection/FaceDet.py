#for elaborate comments on logic refer to source file for
#face detection in videos

#if OpenCV runs out of memory, choose to resize the source image by a 
#factor of 2 or 3

#For portraits or images with large faces, the parameters of the Classifier are 
#usually in the range of ~1.05 and ~6. For group photos with smaller faces, choose 
#larger values of these parameters as used here

#Resize output image if it doesn't fit your display	

import cv2
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("one-tree-hill-main.jpg")
img=cv2.resize(img, ((img.shape[1]//2), int(img.shape[0]/2)))
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(grayImg, scaleFactor=1.17, minNeighbors=20)
for x, y, w, h in faces: img=cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 4)
#img=cv2.resize(img, ((img.shape[1]//2), int(img.shape[0]/2)))
cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()