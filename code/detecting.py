import cv2
import sys
 
cascadePath = "dogdetector.xml"
dogCascade = cv2.CascadeClassifier(cascadePath)
 
cam = cv2.VideoCapture(0)
anterior = 0
while True:
    # Process each frame
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dogs = dogCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40))
 
    # Draw a rectangle around the faces
    for (x, y, w, h) in dogs:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
 
    if anterior != len(dogs):
        anterior = len(dogs)
 
    cv2.imshow('Video', frame)
 
 
    #Press Q to quit
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
 
    # Display video
    cv2.imshow('Video', frame)
 
cam.release()
cv2.destroyAllWindows()