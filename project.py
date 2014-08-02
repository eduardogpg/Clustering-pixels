# -*- encoding: utf-8 -*-
import pygame, sys

import numpy as np
import cv2

from pygame.locals import *
from os import listdir

from Clases import k_means

def loadImage(listPath):
	imageList = []
	for x in range(0, len(listPath)):
		imageList.append( pygame.image.load( listPath[x] ) )
	return imageList

def listAllImage(path):

	listImageName = []
	for archivo in listdir(path):
		if archivo[-2:] != 'py' and archivo[-2:] != 'db':
			listImageName.append(path+archivo)
	return listImageName

def scannImage(image):

	piexelsList = []
	counx = 0;
	for x in range(image.get_width()):
		count = 0
		for y in range(image.get_height()):
			if (255,255,255,255) != image.get_at(( x,y )):
				count +=1
		piexelsList.append(count)

	return piexelsList

def getRGBList(pixel):
	listRGB = []
	listRGB.append(pixel.r)
	listRGB.append(pixel.g)
	listRGB.append(pixel.b)
	return listRGB

def setMatrixOfPixels(image):
	Matriz = []
	for x in range(image.get_width()):
		for y in range(image.get_height()):
			Matriz.append( getRGBList( image.get_at ( (x,y) ) ) )
	return Matriz

def toInteger(Matriz):
	currentMatriz = []
	for lista in Matriz:
		listaEnteros  = []
		for valor in lista:
			listaEnteros.append ( int(valor))
		currentMatriz.append(listaEnteros)

	return currentMatriz


def startAlgorithm(Matriz):
	print "Comenzando Algoritmo  . . ."

	closter = k_means(Matriz, 5)
	closter.algoritmo()
	return makeListColors (toInteger (closter.getMatrizRGBCentroides())), closter.getMatrizResultados()

def makeListColors(MatrizRGB):
	print "Creando Colores  . . ."
	listaColores = []
	for lista in MatrizRGB:
		listaColores.append( tuple(lista) )
	return listaColores

def tratamientoImagen(imagen, listaColores, MatrizPixeles):
	pass

def graphics():
	count = 0
	algorithmFlag = False

	listaColores = []
	matrizGrupoPix = []

	pygame.display.set_caption('Final Project')
	listPath = listAllImage("Imagenes/")
	listImages = loadImage( listPath )

	backGround = listImages[0]
	myWindows = pygame.display.set_mode(( backGround.get_size() ))

	listaColores = []
	color = [0,0,0]

	while True:
		
		if algorithmFlag == False:
			myWindows.blit(backGround,(0,0))
		else:
			myWindows.fill( color )
		
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_RIGHT:
					count +=1
					if algorithmFlag == False:
						if count > len(listImages)-1:
							count = 0
						backGround = listImages[count]
						myWindows = pygame.display.set_mode(( backGround.get_size() ))					
					else:
						if count > len(listaColores)-1:
							count=0
						color = listaColores[count]
						myWindows = pygame.display.set_mode(( 300,300 ))

				elif event.key == pygame.K_LEFT:
					count -=1
					if algorithmFlag == False:
						if count < 0:
							count = len(listImages)-1
						backGround = listImages[count]
						myWindows = pygame.display.set_mode(( backGround.get_size() ))	
					
					else:
						if count<0:
							count = len(listaColores)-1
						color = listaColores[count]
						myWindows = pygame.display.set_mode(( 300,300 ))

				elif event.key == pygame.K_SPACE:
					if algorithmFlag == False:
						listaColores , matrizGrupoPix= startAlgorithm( setMatrixOfPixels(backGround) )
						count = 0
						color = listaColores[count]
						algorithmFlag = True
						myWindows = pygame.display.set_mode(( 300,300 ))

						

		
		pygame.display.update()

pygame.init()
graphics()