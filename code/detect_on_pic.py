import cv2 as cv
import numpy as np

cascadePath = "dogdetector.xml"
dogCascade = cv.CascadeClassifier(cascadePath)

img = cv.imread('\images\dog_on_road2.jpg')
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.namedWindow('img',cv.WINDOW_NORMAL)
cv.waitKey(10000)
#dogs = dogCascade.detectMultiScale(gray,1.3,5)

#for (x, y, w, h) in dogs:
 #   cv.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 2)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()