import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
'''
convert the image from gray to black and white.
'''
fname = os.listdir('/Users/ruisi/Desktop/496/cmput414-project/code/reconstruct/Segmentated_JPG')
imlist=[]
for i in fname:
    img = cv2.imread('/Users/ruisi/Desktop/496/cmput414-project/code/reconstruct/Segmentated_JPG/'+str(i),0)
    if img is not None:
        imlist.append(img)
    else:
        print(str(i)+" is not readable")
print(len(imlist))
seq = 36
for img in imlist:
    seq+=1
    h,w = img.shape
    (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    lis=[]
    for i in im_bw:
        for j in i:
            if j not in lis:
                lis.append(j)

    plt.imshow(im_bw),plt.title("read?")
    plt.show()

    step1= np.zeros((h,w))


    t = 0

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
        print('to select muti value use , to split them')
        ch = raw_input()
        if str(ch) != 'n':
            chl = str(ch).split(",")
            item = []
            item2 = []
            listemp=[]
            listemp2=[]
            for i in chl:
                item.append(temp[int(i)])
                item2.append(temp2[int(i)])
            for i in temp:
                listemp.append(i.tolist())
            for i in item:
                idx = listemp.index(i.tolist())
                listemp.remove(listemp[idx])
                temp = []
                for i in listemp:
                    temp.append(np.array(i))
            for i in item2:
                idx = temp2.index(i)
                temp2.remove(temp2[idx])
        else:
            break
    cv2.imwrite(str(seq)+'.jpeg',step2)
