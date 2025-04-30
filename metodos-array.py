import numpy as np

# Criação de arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([[1, 2, 3], [4, 5, 6]])

# Métodos mais comuns:

# 1. reshape - Redimensiona o array
array_reshape = array1.reshape((5, 1))

# 2. flatten - "Achata" o array multidimensional em um vetor
array_flatten = array2.flatten()

# 3. transpose - Transpõe as dimensões do array
array_transpose = array2.transpose()
print(array_transpose)

# 4. concatenate - Concatena dois ou mais arrays
array_concatenado = np.concatenate((array1, array1))



# 5. split - Divide um array em sub-arrays
arrays_divididos = np.split(array1, 5)

# 6. arange - Cria arrays com valores espaçados uniformemente
array_arange = np.arange(0, 10, 2)

# 7. linspace - Cria arrays com valores igualmente espaçados
array_linspace = np.linspace(0, 1, 5)

# 8. sum - Soma todos os elementos
soma = array1.sum()



# 9. mean - Média dos elementos
media = array1.mean()

# 10. std - Desvio padrão dos elementos
desvio_padrao = array1.std()

# 11. sort - Ordena o array
array_ordenado = np.sort(array2, axis=1)

# 12. unique - Retorna os elementos únicos
elementos_unicos = np.unique(array2)



# 13. where - Condicional para seleção de elementos
indices_maiores_que_2 = np.where(array1 > 2)

# 14. clip - Limita os valores do array dentro de um intervalo
array_clipped = np.clip(array1, 2, 4)

# 15. astype - Converte o tipo de dados
array_float = array1.astype(float)