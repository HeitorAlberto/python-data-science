import pandas as pd

dados = {	"Estado": ["Santa Catarina", "Rio de Janeiro", "Tocantins", "Bahia", "Minas Gerais"],
			"Ano": [2004, 2005, 2006, 2007, 2008],
			"Taxa Desemprego": [1.5,1.7,1.6,2.4,2.7]}



# DATAFRAME 1 - convertendo o dicionário para dataframe
df = pd.DataFrame(dados)


# Imprimindo coluna específica
#print(df["Estado"])


# DATAFRAME 2 - Reorganizando a posição das colunas
df2 = pd.DataFrame(dados, columns = ["Estado", "Taxa Desemprego", "Ano"])


print(df2.describe())