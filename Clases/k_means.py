from random import randint
import math

#Cambiar valores a 1
#Checar por que siempre da los mismos resultados 

class centroide():
	def __init__(self, coordenadas):
		self.coordenadas = coordenadas
		self.viejasCoordenadas = []

	def promedio(self,lista):
	
		for posC in range(0, len(self.coordenadas)):
			suma = 0.0
			for pos in range(0,len(lista)):
				suma = suma + lista[pos][posC]
			self.coordenadas[posC] = suma / len(lista)

		if self.coordenadas == self.viejasCoordenadas:
			return True
		else:
			self.viejasCoordenadas = self.coordenadas
			return False

	def getCoordenadas(self):
		return self.coordenadas

class k_means():
	def __init__(self, listaIndividuos, numeroClases):
		self.listaIndividuos = listaIndividuos

		self.listaCentroides = self.establecerCentroides(numeroClases)
		self.MatrizResultados = []

	def establecerCentroides(self, numeroClases):
		listaAux = []
		for pos in range(0, numeroClases):
			nuevoCentroide = centroide(self.listaIndividuos[randint(0, len(self.listaIndividuos)-1)])
			listaAux.append(nuevoCentroide)
		return listaAux

	def algoritmo(self):
		bandera = False
		while bandera == False:
			
			MatrizResultados = []
			for pos in range(0, len(self.listaCentroides) ):
				MatrizResultados.append([])

			
			MatrizDitancias = []
			for posCentroide in range(0, len(self.listaCentroides)):
				centroideActual = self.listaCentroides[posCentroide]

				listaDistanciaCentroides = []

				for posIndividuos in range(0, len(self.listaIndividuos)):
					individuo = self.listaIndividuos[posIndividuos]
					listaDistanciaCentroides.append ( self.calcularDistancia( centroideActual.getCoordenadas(), individuo ) )
				
				MatrizDitancias.append(listaDistanciaCentroides)

			for posIndividuos in range(0, len(self.listaIndividuos)):
				listaValores = []
				for posMa in range(0, len(MatrizDitancias)):
					listaValores.append(MatrizDitancias[posMa][posIndividuos])

				pos = self.obtenerPosicionMenor(listaValores)
				listaAux = MatrizResultados[pos]
				listaAux.append(self.listaIndividuos[posIndividuos])
				MatrizResultados[pos] = listaAux


			p = True
			for posCentroide in range(0, len(self.listaCentroides)):
				centroide = self.listaCentroides[posCentroide]
				if centroide.promedio(MatrizResultados[posCentroide]) != True:
					p=False

			if p == True:
				self.MatrizResultados = MatrizResultados
				bandera = True
	
	def calcularDistancia(self, listaUno, listaDos):
		distancia = 0
		for pos in range(0, len(listaUno)):
			distancia = distancia + ((listaDos[pos] - listaUno[pos])** 2)
		
		return math.sqrt( distancia )


	def obtenerPosicionMenor(self, lista):
		posMenor = 0
		menor = lista[posMenor]
		for pos in range(0, len(lista)):
			valor = lista[pos]
			if valor < menor:
				menor = valor
				posMenor = pos

		return posMenor

	def mostrarResultados(self):
		print "cluster size : \n"	
		
		for lista in self.MatrizResultados:
			print lista
			print "\n\n\n\n\n\n\n"
	
	def getMatrizResultados(self):
		return self.MatrizResultados

	def getMatrizRGBCentroides(self):
		Matriz = []
		for centroideA in self.listaCentroides:
			Matriz.append( centroideA.getCoordenadas() )
		return Matriz

	def posMayor(self, lista):
		posMayor = 0
		mayor = lista[posMayor]

		for pos in range(0, len(lista)):
			valor = lista[pos]
			if valor > mayor:
				posMayor = pos
				mayor = valor

		return posMayor