from random import randint
import math


class centroide():
	def __init__(self, position):
		self.position = position
		self.oldPosition = []

	def average(self,pointList):
		for posC in range(0, len(self.position)):
			Sum = 0.0
			for pos in range(0,len(pointList)):
				Sum = Sum + pointList[pos][posC]
			self.position[posC] = Sum / len(pointList)

		if self.position == self.oldPosition:
			return True
		else:
			self.oldPosition = self.position
			return False

	def getposition(self):
		return self.position