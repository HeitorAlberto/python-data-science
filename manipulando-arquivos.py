import os
import numpy as np

dados = os.path.join("dados.csv")

x = np.loadtxt(dados, delimiter = ',', usecols = (0,1,2), skiprows= 1)
#skiprows serve para ignorar a linha 1 (cabeçalho da tabela)


a, b = np.loadtxt(dados, delimiter = ',', usecols = (0,1), skiprows = 1, unpack = True)
# unpack permite que cada coluna seja armazenada em um array específico (a e b).


print(x)
print(a)
print(b)