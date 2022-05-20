'''

Desenvolvido por andre.rsouza no dia 19/05/2022
Email: andredarochasouza.12345@gmail.com

Algoritmo K-Nearest Neighbors em Python

'''

# Função que calcula a distância euclidiana entre duas listas de números (sem considerar a ultima posição)
def distancia_euclidiana(dataset_linha, amostra):
    distancia = 0
    for i in range(len(dataset_linha) - 1):
        distancia += (dataset_linha[i] - amostra[i]) ** 2
    return distancia ** (1 / 2)


# Função que retorna uma lista com as distancia euclidiana calculadas (dataset, amostra)
def calcula_distancias_euclidianas(dataset, amostra):
    return [distancia_euclidiana(dataset[i], amostra) for i in range(len(dataset))]
            

# Função que classifica uma amostra de acordo com o dataset 
def classificar_knn(k, dataset, amostra):
    distancias = calcula_distancias_euclidianas(dataset, amostra)
    indices = [i[0] for i in sorted(enumerate(distancias), key=lambda x: x[1])]
    return [dataset[i] for i in indices[:k]]