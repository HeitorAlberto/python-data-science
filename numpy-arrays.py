import numpy as np

np.sqrt(9)  #Raiz quadrada de 9: 3


x = np.array([1, 2, 3, 4])

print(x)              #[1 2 3 4]
print(type(x))        #<class 'numpy.ndarray'>
print(np.ndim(x))     # 1 (apenas uma dimensão)


x[0]      #primeiro elemento
x[-1]     #último elemento
x[1:3]    #Acessa o elemento 1 e 2


y[0:8:2]    #Acessa os elementos do intervalo de 2 em 2


#MATRIZ DE LISTAS
A = [[3, 2], [5, 3]]
A[0]     #Acessa todos os valores da primeira lista (3, 2)
A[0][1]    #Acessa a primeira lista mas retorna apenas o seu segundo elemento (2)



#MATRIZ DE ARRAYS
B = np.array([[5, 3],[1, -3]])

print(np.ndim(x))     # 2 (duas dimensões)




