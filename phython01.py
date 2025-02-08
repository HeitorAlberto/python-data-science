print(df.head())  		      # Mostra as primeiras 5 linhas
print(df.info())  		      # Exibe informações gerais, incluindo valores nulos
print(df.describe())  	    # Estatísticas descritivas das colunas numéricas




df.isnull().sum()  				# Conta os valores nulos por coluna



df = df.dropna() 				          # Remove linhas com valores ausentes
df = df.dropna(axis=1)  		      # Remove colunas com valores ausentes




df = df.fillna("Desconhecido")  							              # Substitui valores ausentes por uma string
df["coluna"] = df["coluna"].fillna(df["coluna"].mean())  	  # Preenche com a média da coluna





df = df.drop_duplicates() 					 	          # Remove linhas duplicadas
df = df.drop_duplicates(subset=["coluna"])  	  # Remove duplicatas com base em uma coluna específica




df["coluna"] = df["coluna"].astype(str)  						          # Converte para string
df["coluna"] = pd.to_numeric(df["coluna"], errors="coerce")  	# Converte para número (substitui erros por NaN)
df["data"] = pd.to_datetime(df["data"])  						          # Converte para formato de data




df["coluna"] = df["coluna"].str.replace("[^0-9]", "", regex=True)  			# Remove caracteres não numéricos
df["coluna"] = df["coluna"].str.strip()  								            	  # Remove espaços extras no início e no fim





df = df.rename(columns={"coluna_antiga": "coluna_nova"})		# Renomeia coluna



df["coluna"] = df["coluna"].apply(lambda x: x.upper())  		# Converte para maiúsculas
df["coluna"] = df["coluna"].apply(lambda x: x * 2)  			  # Dobra o valor da coluna


df = df[df["coluna"] > 10]  							                    # Mantém apenas linhas onde a coluna tem valor maior que 10
df = df[df["coluna"].str.contains("texto", na=False)]        	# Filtra por texto na coluna




df.to_csv("dados_limpos.csv", index=False)  			# Salva sem o índice
df.to_excel("dados_limpos.xlsx", index=False)
