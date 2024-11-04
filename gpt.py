from itertools import permutations, product
from collections import deque

grafo = {
    1: [3, 2],
    2: [],
    3: [5],
    4: [2],
    5: [6, 2, 4],
    6: []
}
"""
ideia: o algoritmo tem outputs diferentes dependendo da ordem dos vizinhos.
grafo = {
    1: [3, 2],
    2: [],
    3: [5],
    4: [2],
    5: [6, 2, 4],
    6: []
}
vai ter um output diferente de:
grafo = {
   1: [3, 2],
   2: [],
   3: [5],
   4: [2],
   5: [2, 4, 6],
   6: []
}
Então, podemos fazer permutações dos vizinhos de cada vértice e subtrair esse output da lista de outputs possíveis.
"""

#algoritmo do slide (pagina 15)
def ordenacao_topologica(grafo):
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

def eh_ordenacao_topologica_valida(ordem, grafo):
    posicao = {v: i for i, v in enumerate(ordem)}
    return all(posicao[v] < posicao[w] for v in grafo for w in grafo[v])

def obter_ordenacoes_topologicas_validas(grafo):
    return [list(perm) for perm in permutations(grafo) if eh_ordenacao_topologica_valida(perm, grafo)]

def obter_ordens_possiveis_do_algoritmo(grafo):
    variacoes_grafo = [list(permutations(vizinhos)) for vizinhos in grafo.values()]
    saidas_possiveis = set()

    for variacao in product(*variacoes_grafo):
        novo_grafo = {v: list(variacao[i]) for i, v in enumerate(grafo)}
        saida_ordenada = tuple(ordenacao_topologica(novo_grafo))
        saidas_possiveis.add(saida_ordenada)

    return [list(saida) for saida in saidas_possiveis]

def encontrar_ordenacoes_impossiveis(grafo):
    todas_ordenacoes_validas = obter_ordenacoes_topologicas_validas(grafo)
    saidas_possiveis = obter_ordens_possiveis_do_algoritmo(grafo)
    ordenacoes_impossiveis = [ordem for ordem in todas_ordenacoes_validas if ordem not in saidas_possiveis]

    return saidas_possiveis, ordenacoes_impossiveis

ordenacoes_possiveis, ordenacoes_impossiveis = encontrar_ordenacoes_impossiveis(grafo)

print("ordenações topológicas produzidas pelo grafo no algoritmo:")
for ordem in ordenacoes_possiveis:
    print(ordem)

print("ordenações impossíveis pelo algoritmo:")
for ordem in ordenacoes_impossiveis:
    print(ordem)
