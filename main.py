import cv2
import numpy as np
minyon=cv2.imread("sungerbob.png")
cv2.imshow("sungerbob.png",minyon)
cv2.waitKey()

sunger_bob=cv2.imread("sungerbob.png",0)
cv2.imshow("sungerbob.png",sunger_bob)
cv2.waitKey()

histBoyut=256
hiatAralık=(0,256)

Hist = np.zeros(256)
[w,h]=sunger_bob.shape

for u in range(0,w):
    for v in range(0,h):
        tut=sunger_bob[u,v]
        Hist[tut]= tut+1

cv2.waitKey()