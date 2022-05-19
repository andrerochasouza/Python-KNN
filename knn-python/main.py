'''

Desenvolvido por andre.rsouza no dia 19/05/2022
Email: andredarochasouza.12345@gmail.com

Algoritmo K-Nearest Neighbors em Python

'''

import knn_python as knn

a = [ 1.0, 1.0, 3.0, 4.0, 5.0, 1.0 ]
b = [ 2.0, 1.0, 4.0, 5.0, 5.0, 1.0 ]
c = [ 1.0, 2.0, 5.0, 4.0, 3.0, 1.0 ]
d = [ 1.0, 2.0, 5.0, 5.0, 5.0, 1.0 ]
e = [ 5.0, 4.0, 2.0, 1.0, 1.0, 0.0 ]
f = [ 4.0, 5.0, 1.0, 1.0, 2.0, 0.0 ]
g = [ 5.0, 5.0, 1.0, 1.0, 1.0, 0.0 ]

matrix = [a, b, c, d, e, f, g]

amostra = [ 3.0, 3.0, 2.0, 1.0, 1.0 ]

print(matrix)
