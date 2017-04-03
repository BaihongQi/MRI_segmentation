import numpy as np
import cv2
from matplotlib import pyplot as plt
img =cv2.imread("test.jpg").astype(np.float32)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h,w = img.shape
print (h,w)

imgnew = np.zeros((h,w))
refrence = np.ones((h/2,(w/2)))
imgnew[(h/4):(3*h/4),(w/4):(3*w/4)] = refrence
imgout = np.multiply(img,imgnew)
refcolor = imgout[h/3][w/2]
print(refcolor)
count =0
count2 = 0
while count < h-1:
    while count2<w-1:
        if imgout[count][count2] >refcolor+10 or imgout[count][count2] <refcolor-10:
            imgout[count][count2] = 1
        count2+=1
    count+=1
    count2=0

#contours= cv2.findContours(imgout,cv2.RETR_FLOODFILL,cv2.CHAIN_APPROX_SIMPLE)[1]
#temp= []
#for contour in contours:
 #   area = cv2.contourArea(contour)
  #  if area>100:
   #     temp.append(contour)
#cv2.drawContours(imgout,temp,-1,(255,0,0),1)
plt.imshow(imgnew),plt.title("zeros")
plt.show()
plt.imshow(imgout),plt.title("huehue")
plt.show()
