import json

x = {"chave1": "valor1", "chave2": "valor2"}

json.dumps(x) #converte o dicionário em um objeto json

#CRIANDO O ARQUIVO
with open('arquivos/dados.json', 'w') as arquivo:
	arquivo.write(json.dumps(x))


#LENDO O ARQUIVO
with open('arquivos/dados.json', 'w') as arquivo:
  texto = arquivo.read()
  dados = json.loads(texto)

print(dados)
