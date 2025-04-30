import numpy as np


a = np.array([
	[

		[1,2,3,4],
		[5,6,7,8],
		[9,10,11,12]
	],
	[
		[13,14,15,16],
		[17,18,19,20],
		[21,22,23,24]

	]

])

# O array acima é uma lista com dois elementos (cada um com 3 listas de números)
# O índice 0 permite acessar o primeiro grupo [1 2 3 4] [5 6 7 8] [9 10 11 12]
# O índice 1 permite acessar o segundo grupo [13 14 15 16] [17 18 19 20] [21 22 23 24]



print(a)
print(a.ndim)		#Retorna o número de dimensões
print(a.shape)		#Retorna o número de linhas e colunas
