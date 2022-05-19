'''

Desenvolvido por andre.rsouza no dia 19/05/2022
Email: andredarochasouza.12345@gmail.com

Algoritmo K-Nearest Neighbors em Python

'''

import math

# Função que calcula a distância euclidiana entre duas lintas com pontos.

def distancia_euclidiano(ponto_1, ponto_2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(ponto_1, ponto_2)) ** 0.5

# Função que retorna uma lista com as distancia euclidianas com os pontos

def calc_dataset(dataset, amostra):

    calc_dataset_euclidiano = []

    for i in range(len(dataset)):
        treinamento_posicao = []
        for j in range(len(amostra)):
            treinamento_posicao.append(dataset[i][j])
        
        calc_dataset_euclidiano.append(distancia_euclidiano(amostra, treinamento_posicao))
    
    return calc_dataset_euclidiano
