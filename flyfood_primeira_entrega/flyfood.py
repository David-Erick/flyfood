from itertools import permutations

with open("entrada_flyfood.txt", "r") as arquivo:
    arquivo_linha = arquivo.readlines()

arquivo_linha_sem_parametros = arquivo_linha[1:]
matriz = [linha.split() for linha in arquivo_linha_sem_parametros]

posicoes_letras = {}

for i, linha in enumerate(matriz):
    for j, elemento in enumerate(linha):
        if elemento.isalpha():
            posicoes_letras[elemento] = (i, j)


def calcular_distancia(letra1, letra2):
    return abs(letra1[0] - letra2[0]) + abs(letra1[1] - letra2[1])

pontos_entrega = list(posicoes_letras.keys())
pontos_entrega.remove('R')  

resultados = []

for permutacao in permutations(pontos_entrega):
    permutacao = ('R',) + permutacao + ('R',) 
    custo_total = 0
    rota = []
    for i in range(len(permutacao) - 1):
        custo_entre_letras = calcular_distancia(posicoes_letras[permutacao[i]], posicoes_letras[permutacao[i + 1]])
        custo_total += custo_entre_letras
        rota.append((permutacao[i], permutacao[i + 1], custo_entre_letras))

#como nao tem como fazer a posição do ultimo termo "ultimo elemento" +1 no append anterior, para fazer a distancia dele com "R" adiciono diretamnete a distancia de R para R  
    custo_total += calcular_distancia(posicoes_letras[permutacao[-1]], posicoes_letras['R'])  
    rota.append((permutacao[-1], 'R', calcular_distancia(posicoes_letras[permutacao[-1]], posicoes_letras['R'])))  
    resultados.append((rota, custo_total))

#encontrando a melhor rota
melhor_rota = min(resultados, key=lambda elem: elem[1])

melhor_caminho = ''.join([letra for letra, i, i in melhor_rota[0]])
print(f"Melhor rota: {melhor_caminho}: com o custo de: {melhor_rota[1]} dronometros")
