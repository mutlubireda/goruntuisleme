
import cv2
import numpy as np

sunger=cv2.imread("sungerbob.png",0)
cv2.imshow("normal",sunger)

np = np.max(sunger)

w,h = sunger.shape

for i in range(0,w):
    for j in range(0,h):
        hist=np-sunger[i,j]
        sunger[i,j]=hist

cv2.imshow("inverted",sunger)
cv2.waitKey()