import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt
import cPickle as pk

def segmentImage(img,threshold):
	'''This function segments an image and returns array or images. Each element is a seperated character from the image'''

	'''Threshold is the number of white pixels in a column between 2 characters'''

	length=len(img)
	lines=[]
	chars=[]
	
	for i in range(length-1):
		'''To horizonatlly segment the image. and stores the images in 'lines' '''
		if 255 not in img[i] and 255 in img[i+1]:
			'''Denotes the first row of the image where the line starts(top)'''
			start_row=i+1
			for k in range(start_row,length-1):
				if 255 in img[k] and 255 not in img[k+1]:
					'''Denotes the end row of the image where the line ends.(bottom)'''
					end_row=k
					line=img[start_row:end_row+1]
					lines.append(line)
					i=end_row+1
					break


	'''Now seperate each chracters in each line and store each character as seperate image in an array'''
	for line in lines:
		line=line.transpose()
		for i in range(len(line)-1):
			'''To horizonatlly segment the image. and stores the images in 'lines' '''
			if 255 not in line[i] and 255 in line[i+1]:
				'''Denotes the first row of the image where the line starts(top)'''
				start_row=i+1
				for k in range(start_row,len(line)-1):
					if 255 in line[k] and 255 not in line[k+1]:
						'''Denotes the end row of the image where the line ends.(bottom)'''
						end_row=k
						char=line[start_row:end_row+1]
						chars.append(char)
						i=end_row+1
						break
	
	for i in range(len(chars)):
		chars[i]=chars[i].transpose()
		chars[i]=cv2.resize(chars[i],None,fx=(float(25)/len(chars[i][0])), fy=(float(25)/len(chars[i])))
		(thresh, chars[i]) = cv2.threshold(chars[i], 128, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

		'''cv2.imshow('image',chars[i])
		cv2.waitKey(0)
		cv2.destroyAllWindows()'''
	return chars

def converttoVector(chars,vector):
	val=1
	for char in chars:
		char=char.reshape(1,625)
		vect=np.array([char[0]])
		vector.append(vect)
	return vector


def main():
	img=cv2.imread(sys.argv[1],cv2.CV_LOAD_IMAGE_GRAYSCALE)
	(thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

	chars=segmentImage(img,0)
	vector=[]
	vector=converttoVector(chars,vector)
	f=open("OCRNetwork2.obj",'rb')
	f1=open("Classifier.obj",'rb')
	MLP=pk.load(f1)
	OCR=pk.load(f)
	results=[]
	w='abcdefghijklmnopqrstuvwxyz'
	for char in vector:
		res=OCR.predict(char)
		r=MLP[w[res-1]].predict(char)
		results.append(r[0])
	count={}
	for i in range(len(results)):
		if results[i] in count:
			count[results[i]]+=1
		else:
			count[results[i]]=1
	ma=0
	f=0
	fonts=['Arial Black','Comic Sans MS', 'Gabriola','Impact','Tempus Sans ITC','Calibri','Harrington','Monotype Corsia','Ravie','Times New Roman']
	for key in count:
		if count[key]>ma:
			ma=count[key]
			f=key
	print fonts[f-1]
	'''cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()'''
main()
