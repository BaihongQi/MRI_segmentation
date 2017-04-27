import numpy as np
import cv2
from matplotlib import pyplot as plt
img =cv2.imread("mybrain.jpg",0)#.astype(np.float32)
#img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
h,w = img.shape
#print (h,w)
plt.imshow(img),plt.title("read?")
plt.show()
imgnew = np.zeros((h,w))
refrence = np.ones((h/2,(w/2)))
imgnew[(h/4):(3*h/4),(w/4):(3*w/4)] = refrence
imgout = np.multiply(img,imgnew)
refcolor = imgout[h/3][w/2]
#print(refcolor)
count =0
count2 = 0
L= []
for i in img:
	for j in i:
		if j not in L:
			L.append(j)
print(len(L))
while count < h-1:
    while count2<w-1:
        if imgout[count][count2] >refcolor+40 or imgout[count][count2] <refcolor-40:
            imgout[count][count2] = 0
        count2+=1
    count+=1
    count2=0
imgout = np.uint8(imgout)
imgoutc = np.copy(imgout) 
#imgout2 = cv2.adaptiveThreshold(imgout, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 0)
#imgout = cv2.cvtColor(imgout,cv2.COLOR_RGB2GRAY)
#imgout = cv2.cvtColor(imgout,cv2.COLOR_RGB2GRAY)
contours= cv2.findContours(imgoutc,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]

temp= []
for contour in contours:
    area = cv2.contourArea(contour)
    if area>100:
        temp.append(contour)
cv2.drawContours(imgout,temp,-1,(255,0,0),1)
'''
for contour in contours:
	x,y,w,h = cv2.boundingRect(contour)
	if w <50 and h <50:
		imgout[y:y+h,x:x+w] = imgnew[y:y+h,x:x+w]
'''
plt.imshow(imgoutc),plt.title("imgoutc")
plt.show()
plt.imshow(imgout),plt.title("results")
plt.show()
