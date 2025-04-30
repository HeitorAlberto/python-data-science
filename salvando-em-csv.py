import pandas as pd

# Leitura do CSV
df = pd.read_csv('dados.csv')

# Modificações no DataFrame
df['nova_coluna'] = df['coluna_existente'] * 2

# Salvando as modificações no mesmo arquivo (sobrescreve)
df.to_csv('dados.csv', index=False)

# Ou salvando em um novo arquivo
df.to_csv('dados_modificado.csv', index=False)
