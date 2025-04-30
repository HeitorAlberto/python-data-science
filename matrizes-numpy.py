import numpy as np


# Lista de listas
lista = [[1,2,3], [4,5,6], [7,8,9]]



m1 = np.matrix(lista) # A lista foi convertida em uma matriz

print(type(m1))	# numpy.matrix
print(np.shape(m1)) # (3, 3) linhas e colunas
print(m1.size)	# 9 elementos




print("-----------------------------------------------------------------------------------")




a = np.array(lista)

print(a)
print(type(a))
print(np.max(a), "(maior valor)")
print(a.itemsize, "(bytes por elemento)") # Retorna o tamanho em bytes de cada elemento do array
print(a.nbytes, "(total de bytes do array)") # Retorna o total de bytes do array
print(a.ndim, "dimensões") # Retorna o número de dimensões do array
