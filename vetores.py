'''
	Vetores: estrutura unidimensional.
	Matriz: estrutura multidimensional (linhas e colunas).

'''


lista_de_compras = ["Arroz", "Feijão", "Leite", "Ovos"]
lista_de_valores = [10, 5, 8, 12, 3]

# Adição de elemento no final da lista
lista_de_compras.append("Farinha")

# Adição de elemento em posição específica
lista_de_compras.insert(0, "Suco")


# Remoção do último elemento
lista_de_compras.pop()

# Remoção de um elemento por posição
lista_de_compras.pop(3)




print(len(lista_de_compras)) # Retorna o número de elementos na lista