'''

Desenvolvido por andre.rsouza no dia 19/05/2022
Email: andredarochasouza.12345@gmail.com

Algoritmo K-Nearest Neighbors para regressão em Python

'''

# Função que calcula duas listas de números (sem considerar a ultima posição) e faltando algum valor
def distancia_euclidiana(dataset_linha, amostra):
    distancias = 0
    for i in range(len(dataset_linha) - 1):
        if amostra[i] != None:
            distancias += (dataset_linha[i] - amostra[i]) ** 2
    return distancias ** 0.5

# Função que retorna uma lista com as distancia euclidiana calculadas (dataset, amostra) faltando um valor
def calcula_distancia_euclidiana_faltante(dataset, amostra):
    return [distancia_euclidiana(dataset[i], amostra) for i in range(len(dataset))]

# Função que descobre a regressão linear de uma amostra de acordo com o dataset
def regressao_knn_media(k, dataset, amostra):
    distancias = calcula_distancia_euclidiana_faltante(dataset, amostra)
    indices = [i[0] for i in sorted(enumerate(distancias), key=lambda x: x[1])]
    map = [dataset[i] for i in indices[:k]]
    media = 0

    for i in range(len(map)):
        for j in range(len(amostra)):
            if amostra[j] == None:
                media += map[i][j]
    return media / k