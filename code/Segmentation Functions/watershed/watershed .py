import numpy as np
def getRegionalMinima(img):
    # add your code here
	row,col= img.shape
	row,col=int(row),int(col)
	rowc=0
	colc=0
	img2=np.copy(img)
	print(row,col)
	marker=0
	while rowc<=row-1:
		while colc <= col-1:
			current= img[rowc][colc]
			lis=[]
			if colc+1<=col-1:

				lis.append(img[rowc][colc+1])
			if colc-1>=0:
				
				lis.append(img[rowc][colc-1])
			if rowc-1>=0:
				
				lis.append(img[rowc-1][colc])
			if rowc-1>=0 and colc+1<=col-1:
				
				lis.append(img[rowc-1][colc+1])
			if rowc-1>=0 and colc-1>=0:
				
				lis.append(img[rowc-1][colc-1])
			if rowc+1<=row-1 and colc-1>=0:
				
				lis.append(img[rowc+1][colc-1])
			if rowc+1<=row-1 and colc+1 <=col-1:
				
				lis.append(img[rowc+1][colc+1])
			if rowc+1 <=row-1:
				
				lis.append(img[rowc+1][colc])
			min= True
			for i in lis:
				
				if i < current:
					min=False
			if min == True:
				marker+=1
				img2[rowc][colc]=marker
			else:
				img2[rowc][colc]=0
			colc+=1
		colc=0
		rowc+=1
	
	return img2
					
			
	pass


def iterativeMinFollowing(img, markers):
    # add your code here
	row,col= img.shape
	row,col=int(row),int(col)
	rowc=0
	colc=0
	img3=np.copy(markers)
	print(row,col)
	count = row*col
	while count>0:
		rowc=0
		colc=0
		while rowc<=row-1:
			while colc <= col-1:
				current= img[rowc][colc]
				lis=[]
				lis1=[]
				if markers[rowc][colc]!=0:
					colc+=1
					continue
				if colc+1<=col-1:
					lis.append(img[rowc][colc+1])
					lis1.append([rowc,colc+1])
				if colc-1>=0:
					lis1.append([rowc,colc-1])
					lis.append(img[rowc][colc-1])
				if rowc-1>=0:
					lis1.append([rowc-1,colc])
					lis.append(img[rowc-1][colc])
				if rowc-1>=0 and colc+1<=col-1:
					lis1.append([rowc-1,colc+1])
					lis.append(img[rowc-1][colc+1])
				if rowc-1>=0 and colc-1>=0:
					lis1.append([rowc-1,colc-1])
					lis.append(img[rowc-1][colc-1])
				if rowc+1<=row-1 and colc-1>=0:
					lis1.append([rowc+1,colc-1])
					lis.append(img[rowc+1][colc-1])
				if rowc+1<=row-1 and colc+1 <=col-1:
					lis1.append([rowc+1,colc+1])
					lis.append(img[rowc+1][colc+1])
				if rowc+1 <=row-1:
					lis1.append([rowc+1,colc])
					lis.append(img[rowc+1][colc])
				L= len(lis)
				found= False
				minum= min(lis)
				idx = lis.index(minum)
				m1,m2= lis1[idx][0],lis1[idx][1]
				if img3[m1][m2]!=0:
					count-=1
					img3[rowc][colc]=img3[m1][m2]
				colc+=1
			colc=0
			rowc+=1
	
	return img3
	pass


