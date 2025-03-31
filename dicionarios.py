#Essa estrutura de dados possui chaves e seus respectivos valores

x = {"Chave0": "valor0", "Chave1": "valor1"}

print(x)   # Retorno o dicionário completo
print(x["chave0"])   # Retorna o valor correspondente da chave informada
print(x.keys()) # Retorna uma lista com as chaves
print(x.values()) # Retorna uma lista com os valores

x["chave2"] = "valor2"    # Se já existir, modifica  /  se não existir, cria um novo par "chave/valor"

y = x.copy()  # y passa a ser uma cópia do dicionário x
y = dict(x) # da mesma forma y passa a ser uma cópia de x


for valor in x.values():
  print(valor)
  #O loop acessa e retorna cada valor

for valor in x.keys():
  print(valor)
  #O loop acessa e retorna cada chave

for chave, valor in x.items():
  print(chave, valor)
  #O loop acessa e retorna cada chave e valor
