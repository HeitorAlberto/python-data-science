# LISTAS
numeros = [10, 5, 9, 12, 27]
times = ["Flamengo", "Palmeiras", "Botafogo", "Grêmio"]

print(numeros[0])    #Retorna o primeiro número (10)
print(numeros[-1)]   #Retorna o último número da lista (27)
print(numeros[0:3])  #Retorna os elementos da posição 0 até 2



print(times[1])     #Retorna o segundo time da lista ("Palmeiras")
print(times[-1])    #Retorna o último time da lista ("Grêmio")
print(times[0:2])   #Retorna os elementos da posição 0 até 1

lista3 = lista1 + lista2      #Concatenação: A variável passa a conter todos os valores da lista 1 e 2


print(numeros[0] + numeros[1])    #Retorna 15 - a soma dos elementos 0 e 1

numeros_copia = numeros.copy()  #O método "copy()" cria uma cópia dos valores para a nova variável         #Este método é do objeto "list" do python

numeros.append(2)          #Adiciona o número 2 no final da lista
numeros.extend([4,8,6))    #Adiciona mais de um elemento no final da lista
numeros.index(10)          #Retorna a posição do elemento 10 na sua primeira aparição na lista 
numeros.count(5)           #Retorna contagem de elementos 5 na lista
numeros.insert(2,5)        #Insere o número 5 na posição 2
numeros.pop(9)             #Remove o número 9
numemros.remove(6)         #Remove o número 6 em sua primeira aparição apenas
numeros.sort()             #Coloca os elementos em ordem crescente
numeros.reverse()          #Inverte a ordem dos elementos
numeros.clear()            #Limpa a lista

