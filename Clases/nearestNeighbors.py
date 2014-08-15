import math

class NearestNeighbors():

	def __init__(self, listaCentroides, matrixIndividuos):
		self.centroidesList = listaCentroides
		self.matrixIndividuos = matrixIndividuos

	def calculateDistance(self,listOne, listTwo):
		distancia = 0
		for pos in range(0, len(listOne)):
			distancia = distancia + ((listTwo[pos] - listOne[pos])** 2)
		return math.sqrt( distancia )


	def getLessPosition(self,lista):
		posMenor = 0
		menor = lista[posMenor]
		for pos in range(0, len(lista)):
			valor = lista[pos]
			if valor < menor:
				menor = valor
				posMenor = pos
		return posMenor

	def algoritm(self):
		MatrixAux = []
		for lista in self.matrixIndividuos:
			listaDistancias = []
			for centroide in self.centroidesList:
				listaDistancias.append ( self.calculateDistance(lista, centroide ) )
			MatrixAux.append( self.getLessPosition(listaDistancias) )

		return MatrixAux
	
