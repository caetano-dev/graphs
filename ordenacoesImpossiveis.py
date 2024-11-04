from itertools import permutations, product
from collections import deque

grafo = {
    1: [3, 2],
    2: [],
    3: [5],
    4: [2],
    5: [6, 4, 2],
    6: []
}
"""
ideia: o algoritmo tem outputs diferentes dependendo da ordem dos vizinhos.
grafo = {
    1: [3, 2],
    2: [],
    3: [5],
    4: [2],
    5: [6, 4, 2],
    6: []
}
vai ter um output diferente de:
grafo = {
   1: [3, 2],
   2: [],
   3: [5],
   4: [2],
   5: [4, 6, 2],   <---------
   6: []
}
Então, podemos fazer permutações dos vizinhos de cada vértice e subtrair esse output da lista de outputs possíveis.
"""

def ordenacao_topologica(grafo):  #algoritmo do slide (pagina 15)
    grau_entrada = {v: 0 for v in grafo}
    for vizinhos in grafo.values():
        for w in vizinhos:
            grau_entrada[w] += 1

    fila = deque([v for v in grafo if grau_entrada[v] == 0])
    ordem_topologica = []

    while fila:
        v = fila.popleft()
        ordem_topologica.append(v)
        for w in grafo[v]:
            grau_entrada[w] -= 1
            if grau_entrada[w] == 0:
                fila.append(w)

    return ordem_topologica

def ordenacao_topologica_valida(ordem, grafo): # vamos verificar se a ordenacao topologica criada eh valida
    posicao = {}
    for i, v in enumerate(ordem):
        posicao[v] = i

    for v in grafo:
        for w in grafo[v]:
            if posicao[v] >= posicao[w]:
                return False
    return True

def obter_ordenacoes_topologicas_validas(grafo):
    ordenacoes_validas = []
    for perm in permutations(grafo): #vamos criar permutacoes dos vertices do grafo para testar
        if ordenacao_topologica_valida(perm, grafo):
            ordenacoes_validas.append(list(perm))
    return ordenacoes_validas

def obter_outputs_possiveis_do_algoritmo(grafo):
    variacoes_grafo = []
    for vizinhos in grafo.values():
        variacoes_grafo.append(list(permutations(vizinhos)))

    saidas_possiveis = set()
    for variacao in product(*variacoes_grafo):
        novo_grafo = {}
        for i, v in enumerate(grafo):
            novo_grafo[v] = list(variacao[i])
        saida_ordenada = tuple(ordenacao_topologica(novo_grafo)) # pegamos todas as ordenações possíveis para esse algoritmo
        saidas_possiveis.add(saida_ordenada)

    return [list(saida) for saida in saidas_possiveis]

def encontrar_ordenacoes_impossiveis(grafo):
    todas_ordenacoes_validas = obter_ordenacoes_topologicas_validas(grafo)
    saidas_possiveis = obter_outputs_possiveis_do_algoritmo(grafo)

    ordenacoes_impossiveis = []
    for ordem in todas_ordenacoes_validas: # vamos selecionar as ordenações impossíveis apenas
        if ordem not in saidas_possiveis:
            ordenacoes_impossiveis.append(ordem)

    return saidas_possiveis, ordenacoes_impossiveis

ordenacoes_possiveis, ordenacoes_impossiveis = encontrar_ordenacoes_impossiveis(grafo)

print("ordenações topológicas produzidas pelo grafo no algoritmo:")
for ordem in ordenacoes_possiveis:
    print(ordem)

print("ordenações impossíveis pelo algoritmo:")
for ordem in ordenacoes_impossiveis:
    print(ordem)
