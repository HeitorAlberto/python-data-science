import numpy as np

x = np.arange(1,10)

print("Valores:", x)
print("Soma dos valores:", np.sum(x))
print("Multiplicação entre os elementos:", np.prod(x))
print("Soma acumulada: ", np.cumsum(x))

print("------------------------------------------")

a1 = np.array([3,2,1])
a2 = np.array([1,2,3])
a3 = np.add(a1, a2)

print("Array 1:", a1)
print("Array 2:", a2)
print("Array 3 como a soma do a1 e a2:", a3)