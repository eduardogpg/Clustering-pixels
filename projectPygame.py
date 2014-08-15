# -*- encoding: utf-8 -*-
import pygame, sys

import math

import numpy as np
import cv2
from PIL import Image
from pygame.locals import *
from os import listdir
from Clases import k_means
from Clases import NearestNeighbors as NN


def loadImage(listPath):
	imageList = []
	for x in range(0, len(listPath)):
		imageList.append( pygame.image.load( listPath[x] ) )
	return imageList

def listAllImage(path):

	listOfNamesofImages = []
	for registry in listdir(path):
		if registry[-2:] != 'py' and registry[-2:] != 'db':
			listOfNamesofImages.append(path+registry)
	return listOfNamesofImages

def getRGBList(pixel):
	listRGB = []
	if pixel.r == 0:
		listRGB.append(1)
	else:
		listRGB.append(pixel.r)

	if pixel.g == 0:
		listRGB.append(1)
	else:
		listRGB.append(pixel.g)

	if pixel.b == 0:
		listRGB.append(1)
	else:
		listRGB.append(pixel.b)
	return listRGB

def setMatrixOfPixels(image):
	Matrix = []
	for x in range(image.get_width()):
		for y in range(image.get_height()):
			Matrix.append( getRGBList( image.get_at ( (x,y) ) ) )
	return Matrix

def toInteger(Matrix):
	currentMatrix = []
	for lista in Matrix:
		IntegerList  = []
		for value in lista:
			IntegerList.append ( int(value))
		currentMatrix.append(IntegerList)
	return currentMatrix


def startNearestNeighbors(Matrix, listaCentroides):
	nearestNeighbors = NN(listaCentroides, Matrix)
	return nearestNeighbors.algoritm()


def startAlgorithmKMeans(Matrix, numeroCentroides):
	cluster = k_means(Matrix, numeroCentroides)
	cluster.algorithm()
	return (toInteger (cluster.getMatrizRGBCentroides()))

def makeListColors(RGBMatrix):
	ColorList = []
	for lista in RGBMatrix:
		ColorList.append( tuple(lista) )
	return ColorList

def sumaValores(tupla):
	suma = 0
	for valor in tupla:
		suma = suma + valor
	return suma

def graphics(numeroCentroides, opcion):
	pygame.init()
	
	count = 0
	flagAlgorithm = False
	dibujar = opcion
	
	ColorList = []
	Matrix = []

	pygame.display.set_caption('Final Project')
	listImages = loadImage( listAllImage("Imagenes/") )

	backGround = listImages[0]
	myWindows = pygame.display.set_mode(( backGround.get_size() ))

	while True:
		myWindows.blit(backGround,(0,0))
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_RIGHT:
					if flagAlgorithm == False:
						count +=1	
						if count > len(listImages)-1:
							count = 0
						backGround = listImages[count]
						myWindows = pygame.display.set_mode(( backGround.get_size() ))					
					
				elif event.key == pygame.K_LEFT:
					
					if flagAlgorithm == False:
						count -=1
						if count < 0:
							count = len(listImages)-1
						backGround = listImages[count]
						myWindows = pygame.display.set_mode(( backGround.get_size() ))
					
					
				elif event.key == pygame.K_SPACE:
					if flagAlgorithm == False:
						print "Comienza el algoritmo de Cluster"
						MarizPixeles = setMatrixOfPixels(backGround)
						
						listaClusters = startAlgorithmKMeans( MarizPixeles ,numeroCentroides )
						ColorList = makeListColors(listaClusters)

						print "Termina el algoritmo de Cluster\n\n"

						if dibujar==True:
							print "Comienza el algoritmo Nearest Neighbors"
							Matrix = startNearestNeighbors( MarizPixeles, listaClusters )
							print "Termina el algoritmo Nearest Neighbors\n\n"
						flagAlgorithm = True
						
						
		if flagAlgorithm==True:
			if dibujar==True:
				print "Se comienza a dibujar"
				contadorPersonal = 0
				for x in range(backGround.get_width()):
					for y in range(backGround.get_height()):
						pygame.draw.circle(backGround, ColorList[ Matrix[contadorPersonal] ], (x, y),1, 0)
						contadorPersonal+=1
				
				pygame.display.update()
				flagAlgorithm = False
				print "Se Termina \n\n"
			
			else:
				size = backGround.get_height() / len(ColorList)
				inicio = 0
				siguiente = inicio + size
				for color in ColorList:
					pygame.draw.rect(backGround, color , (0, inicio , backGround.get_width(), size ))
					inicio = siguiente
					siguiente = inicio + size
				pygame.display.update()
		
		pygame.display.update()

		

if __name__ == "__main__":
	
	if len(sys.argv)==5:
		if int(sys.argv[4]) == 1:
			graphics( int(sys.argv[2]),  True )	
		else:
			graphics( int(sys.argv[2]),  False )	
	else:
		print "Sentencia correcta:"
		print "python ProjectPygame.py centroides n opcion 1/2"
		graphics( 10 ,  True )
