def find_cliques_of_size_3(graph):
    """
    Encontra todas as cliques de tamanho 3 em um grafo.

    :param graph: Dicionário onde a chave é o nó e o valor é uma lista de nós adjacentes
    :return: Lista de cliques de tamanho 3
    """
    cliques = []

    # Lista de todos os nós do grafo
    nodes = list(graph.keys())

    # Gerar manualmente todas as combinações de 3 nós
    n = len(nodes)
    for i in range(n): # vertice atual
        for j in range(i + 1, n): # prox vertice do i
            for k in range(j + 1, n): # prox vertice do j
                u, v, w = nodes[i], nodes[j], nodes[k]
                # Verifica se u, v e w formam uma clique
                # Pega todos os vértices e verifica se eles estão na lista de adjacências uns dos outros
                if (v in graph[u] and w in graph[u] and # Acessa a lista de adjacências de u e verifica se v e w estão lá
                    u in graph[v] and w in graph[v] and # Acessa a lista de adjacências de v e verifica se u e w estão lá
                    u in graph[w] and v in graph[w]): # Acessa a lista de adjacências de w e verifica se u e v estão lá
                    # Achamos uma clique de tamanho 3
                    cliques.append((u, v, w))

    return cliques

# Exemplo de grafo como dicionário de adjacências
# Pode ser uma lista encadeada.
grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C'],
    'E': ['B']
}

# Chamando a função
cliques = find_cliques_of_size_3(grafo)
print("Cliques de tamanho 3:", cliques)
