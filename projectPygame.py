# -*- encoding: utf-8 -*-
import pygame, sys

import math

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

def calculateDistance(listOne, listTwo):
	distancia = 0
	for pos in range(0, len(listOne)):
		distancia = distancia + ((listTwo[pos] - listOne[pos])** 2)
	return math.sqrt( distancia )


def getLessPosition(lista):
	posMenor = 0
	menor = lista[posMenor]
	for pos in range(0, len(lista)):
		valor = lista[pos]
		if valor < menor:
			menor = valor
			posMenor = pos
	return posMenor


def NearestNeighbors(Matrix, listaCentroides):
	MatrixAux = []
	for lista in Matrix:
		listaDistancias = []
		for centroide in listaCentroides:
			listaDistancias.append ( calculateDistance(lista, list(centroide)) )
		MatrixAux.append( getLessPosition(listaDistancias) )

	return MatrixAux
	
def startAlgorithmKMeans(Matrix, numeroCentroides):
	cluster = k_means(Matrix, numeroCentroides)
	cluster.algorithm()
	return makeListColors(toInteger (cluster.getMatrizRGBCentroides()))

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
						ColorList = startAlgorithmKMeans( MarizPixeles ,numeroCentroides )
						
						if dibujar==True:
							Matrix = NearestNeighbors( MarizPixeles, ColorList )
						flagAlgorithm = True
						print "Termina el algoritmo de Cluster"

						
						
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
				print "Se Termina "
			
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

		



if int(sys.argv[2]) == 1:
	graphics( int(sys.argv[1]),  True )	
else:
	graphics( int(sys.argv[1]),  False )	

