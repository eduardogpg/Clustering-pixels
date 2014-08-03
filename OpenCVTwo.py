import numpy as np
import cv2
from Clases import k_means

def recVideo():
	cap = cv2.VideoCapture(0)
	while(True):
	    ret, frame = cap.read()

	    color = cv2.cvtColor(frame,cv2.WINDOW_NORMAL)
	    cv2.imshow('frame',color)

	    k = cv2.waitKey(33)
	    if k == 27:
	    	break
	    elif k == 115:
	    	cv2.imwrite('Demo.png',frame)
	    	break
	cap.release()
	cv2.destroyAllWindows()

def toInteger(Matrix):
	currentMatrix = []
	for lista in Matrix:
		IntegerList  = []
		for value in lista:
			IntegerList.append ( int(value))
		currentMatrix.append(IntegerList)
	return currentMatrix

def startAlgorithm(Matrix ):
	cluster = k_means(Matrix, 5)
	cluster.algorithm()
	return makeListColors (toInteger (cluster.getMatrizRGBCentroides())), cluster.getMatrixResults()

def makeListColors(RGBMatrix):
	print "Creando Colores  . . ."
	ColorList = []
	for lista in RGBMatrix:
		ColorList.append( tuple(lista) )
	return ColorList

def getMatrixRGB(image):
	height, width, depth = image.shape
	
	MatrixRGB = []
	for x in range(0, width):
		for y in range(0, height):
			MatrixRGB.append( list( image[y][x] ) ) #Return BGR 
	
	print MatrixRGB[0]
	return MatrixRGB

def loadImage(path="Demo.png"):
	img = cv2.imread(path,1)
	cv2.imshow('Captura',img)
	listaColores, matrix = startAlgorithm (getMatrixRGB(img))
	
	for valor in listaColores:
		print valor

	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
recVideo()
loadImage()