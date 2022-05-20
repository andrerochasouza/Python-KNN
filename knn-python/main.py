'''

Desenvolvido por andre.rsouza no dia 19/05/2022
Email: andredarochasouza.12345@gmail.com

Algoritmo K-Nearest Neighbors em Python

'''

import knn_python as knn
import regressao_linear_knn as reg


dataset = [[ 1.0, 1.0, 3.0, 4.0, 5.0, "mago" ],
           [ 2.0, 1.0, 4.0, 5.0, 5.0, "mago" ],
           [ 1.0, 2.0, 5.0, 4.0, 3.0, "mago" ],
           [ 1.0, 2.0, 5.0, 5.0, 5.0, "mago" ],
           [ 5.0, 4.0, 2.0, 1.0, 1.0, "guerreiro" ],
           [ 4.0, 5.0, 1.0, 1.0, 2.0, "guerreiro" ],
           [ 5.0, 5.0, 1.0, 1.0, 1.0, "guerreiro" ],
           [ 3.0, 4.0, 1.0, 1.0, 3.0, "guerreiro" ]]


amostra_classificacao = [ 3, 4.6, 2.0, 1.0, 1.0 ]
amostra_regressao = [ 3, 4.6, None, 1.0, 1.0, "guerreiro" ]

print(knn.classificar_knn(3, dataset, amostra_classificacao))
print(reg.regressao_knn_media(3, dataset, amostra_regressao))
