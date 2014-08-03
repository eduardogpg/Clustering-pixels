from random import randint
import math
from centroide import centroide


class k_means():
	def __init__(self, listaIndividuos, numberOfCentroides):
		self.listaIndividuos = listaIndividuos
		self.centroidesList = self.setCentroides(numberOfCentroides)
		self.matrixResults = []

	def setCentroides(self, numberOfCentroides):
		listaAux = []
		for pos in range(0, numberOfCentroides):
			newCentroide = centroide(self.listaIndividuos[randint(0, len(self.listaIndividuos)-1)])
			listaAux.append(newCentroide)
		return listaAux

	def algorithm(self):
		flag = False
		while flag == False:
			
			matrixResults = []
			for pos in range(0, len(self.centroidesList) ):
				matrixResults.append([])

			
			distanceMatrix = []
			for currentCentroide in self.centroidesList:
				distanceListCentroide = []

				for individuo in self.listaIndividuos:
					distanceListCentroide.append ( self.calculateDistance( currentCentroide.getposition(), individuo ) )
				
				distanceMatrix.append(distanceListCentroide)

			for posIndividuos in range(0, len(self.listaIndividuos)):
				valuesList = []
				for posMa in range(0, len(distanceMatrix)):
					valuesList.append(distanceMatrix[posMa][posIndividuos])

				pos = self.getLessPosition(valuesList)
				listaAux = matrixResults[pos]
				listaAux.append(self.listaIndividuos[posIndividuos])
				matrixResults[pos] = listaAux


			p = True
			for posCentroide in range(0, len(self.centroidesList)):
				centroide = self.centroidesList[posCentroide]
				if centroide.average(matrixResults[posCentroide]) != True:
					p=False

			if p == True:
				self.matrixResults = matrixResults
				flag = True
	
	def calculateDistance(self, listOne, listTwo):
		distancia = 0
		for pos in range(0, len(listOne)):
			distancia = distancia + ((listTwo[pos] - listOne[pos])** 2)
		return math.sqrt( distancia )

	def getLessPosition(self, lista):
		posMenor = 0
		menor = lista[posMenor]
		for pos in range(0, len(lista)):
			valor = lista[pos]
			if valor < menor:
				menor = valor
				posMenor = pos

		return posMenor

	
	def getMatrixResults(self):
		return self.matrixResults

	def getMatrizRGBCentroides(self):
		Matriz = []
		for centroideA in self.centroidesList:
			Matriz.append( centroideA.getposition() )
		return Matriz

	def getCentroidesList(self):
		return self.centroidesList