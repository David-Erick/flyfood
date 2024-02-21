with open("entrada_flyfood.txt", "r") as arquivo:
    arquivo_linha = arquivo.readlines()

arquivo_linha_sem_parametros = arquivo_linha[1:]
matriz = [linha.split() for linha in arquivo_linha_sem_parametros]

posicoes_letras = {}

for i, elem in enumerate(matriz):
    for j, elemento in enumerate(elem):
        if elemento.isalpha():
            posicoes_letras[elemento] = (i, j)


def calcular_distancia(letra1, letra2):
    return abs(letra1[0] - letra2[0]) + abs(letra1[1] - letra2[1])

def vizinho_mais_proximo(posicoes_letras, ponto_inicial):
    pontos_restantes = list(posicoes_letras.keys())
    pontos_restantes.remove(ponto_inicial)

    ponto_atual = ponto_inicial
    caminho = [ponto_atual]

    while pontos_restantes:
        distancias = {ponto: calcular_distancia(posicoes_letras[ponto_atual], posicoes_letras[ponto]) for ponto in pontos_restantes}
        ponto_mais_proximo = min(distancias, key=distancias.get)

        caminho.append(ponto_mais_proximo)
        ponto_atual = ponto_mais_proximo
        pontos_restantes.remove(ponto_mais_proximo)

#adiciona o retorno ao ponto inicial 'R'
    caminho.append(ponto_inicial)

    return caminho


#chamando a funcao do visinho mais proximo
caminho_vizinho_proximo = vizinho_mais_proximo(posicoes_letras, 'R')

#distancia total do caminho encontrado
distancia_total = 0

# a cada iteração, calcula a distância entre o ponto 
#atual e o proximo ponto, acumulando o resultado na variavel
for i in range(len(caminho_vizinho_proximo) - 1):
    ponto_atual = caminho_vizinho_proximo[i]
    proximo_ponto = caminho_vizinho_proximo[i + 1]
    distancia_total += calcular_distancia(posicoes_letras[ponto_atual], posicoes_letras[proximo_ponto])


print(f"O caminho do vizinho mais proximo é: {caminho_vizinho_proximo} com a distancia total de: {distancia_total}")