# -*- encoding: utf-8 -*-
import pygame, sys


import numpy as np
import cv2
from PIL import Image
from pygame.locals import *
from os import listdir
from Clases import k_means


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
	listRGB.append(pixel.r)
	listRGB.append(pixel.g)
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

def startAlgorithm(Matrix, numeroCentroides):
	cluster = k_means(Matrix, numeroCentroides)
	cluster.algorithm()
	return makeListColors (toInteger (cluster.getMatrizRGBCentroides())), cluster.getMatrixResults()

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
	next = False

	ColorList = []
	pixelGroup = []

	pygame.display.set_caption('Final Project')
	listPath = listAllImage("Imagenes/")
	listImages = loadImage( listPath )

	backGround = listImages[0]
	myWindows = pygame.display.set_mode(( backGround.get_size() ))

	ColorList = []
	

	while True:
		
		#if flagAlgorithm == False:
		myWindows.blit(backGround,(0,0))
		#else:
		#	myWindows.fill( currentColor )
		
		
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
					else:
						next=True
				elif event.key == pygame.K_LEFT:
					if flagAlgorithm == False:
						count -=1
						if count < 0:
							count = len(listImages)-1
						backGround = listImages[count]
						myWindows = pygame.display.set_mode(( backGround.get_size() ))
					else:
						next=True	
					
				elif event.key == pygame.K_SPACE:
					if flagAlgorithm == False:
						ColorList , pixelGroup= startAlgorithm( setMatrixOfPixels(backGround), numeroCentroides )
						count = 0
						color = ColorList[count]
						#myWindows = pygame.display.set_mode(( 300,300 ))
						flagAlgorithm = True
						print "Algoritmo terminado"

		if flagAlgorithm==True:
			if dibujar==True and next==True:
				if count < len(ColorList)-1:
					print "Comienza a colorear : "+str(count)
					copia = pixelGroup[count]
					for x in range(0, backGround.get_width()):
						for y in range(0,backGround.get_height()):
							if getRGBList( backGround.get_at((x,y)) ) in copia:
								pygame.draw.circle(backGround, ColorList[count], (x, y),1, 0)
								pygame.display.update()
			
					print "Termina\n\n"
					next=False
			
			elif dibujar==False and next==False:
				size = backGround.get_height() / len(ColorList)
				inicio = 0
				siguiente = inicio + size
				for color in ColorList:
					pygame.draw.rect(backGround, color , (0, inicio , backGround.get_width(), size ))
					inicio = siguiente
					siguiente = inicio + size
				pygame.display.update()
		
		pygame.display.update()

		



if int(sys.argv[2]) == 1:
	graphics( int(sys.argv[1]),  True )	
else:
	graphics( int(sys.argv[1]),  False )	

