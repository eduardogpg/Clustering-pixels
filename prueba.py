def posCercano(valorSimpson, lista):
	posMenor = 0
	valorMenor = 10000
	
	for posValor in range(0, len(lista)):
		valor = int (lista[posValor])
		res = valorSimpson- valor
		if res<0:
			res = res * -1
		if  res< valorMenor:
			print "Entro con "+ str(res)
			valorMenor = res
			posMenor = posValor

	
	return posMenor

lista = [15, 18, 99,  88, 100]
numero = 66
print posCercano(numero, lista)