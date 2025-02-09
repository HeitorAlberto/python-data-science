#Essa estrutura de dados possui chaves e seus respectivos valores

fla = {"Nome": "CR Flamengo", "País": "Brasil", "Estado": "Rio de Janeiro", "Fundação": 1895, "Libertadores": 3}

print(fla)   # Retorno: {"Nome": "CR Flamengo", "País": "Brasil", "Estado": "Rio de Janeiro", "Fundação": 1895, "Libertadores": 3}
print(fla["Libertadores"])   # Retorno: 3

fla["Brasileiros"] = 8    #Atribui uma nova chave ("Brasileiros") e seu respectivo valor (8)
