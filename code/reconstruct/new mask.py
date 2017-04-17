import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
'''
convert the image from gray to black and white.
'''
fname = os.listdir('/Users/Ray/Desktop/496/cmput414-project/code/reconstruct/JPEG-data')
#print(fname)
imlist=[]
for i in fname:
    img = cv2.imread('/Users/Ray/Desktop/496/cmput414-project/code/reconstruct/JPEG-data/'+str(i),0)
    if img is not None:
        imlist.append(img)
    else:
        print(str(i)+" is not readable")
print(len(imlist))
seq = 0
for img in imlist:
    seq+=1
    h,w = img.shape
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    lis=[]
    for i in im_bw:
        for j in i:
            if j not in lis:
                lis.append(j)
#    print(len(lis))
#    print(lis)
    plt.imshow(im_bw),plt.title("read?")
    plt.show()

    step1= np.zeros((h,w))


    t = 0
    '''
    while t<5:
        blur = cv2.GaussianBlur(im_bw,(5,5),0)
        im_bw = blur
        t=t+1
    edge =cv2.Canny(im_bw, 30, 150)
    '''
    cnt = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

    ch = 0
    temp = []
    temp2 = []
    for i in cnt:

        area = cv2.contourArea(i)
        if 10000>area>60:
            temp.append(i)
            temp2.append(area)
    while ch != 'n':
        step2= np.zeros((h,w))
        cv2.drawContours(step2,temp,-1,(255,0,0),-1)
        plt.imshow(step2),plt.title("1")
        plt.show()
        print(temp2)
        print("is there anything you would like to remove? choese between 0 to "+str(len(temp)-1))
        ch = raw_input()
        if str(ch) != 'n':
            temp.remove(temp[int(ch)])
            temp2.remove(temp2[int(ch)])
        else:
            break
    cv2.imwrite(str(seq)+'.jpeg',step2)
