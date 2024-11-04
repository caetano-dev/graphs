import random
from collections import defaultdict

def create_large_dag(num_layers=10, nodes_per_layer=10):
    graph = defaultdict(list)
    current_node = 1
    layer_nodes = []

    # Create nodes layer by layer
    for layer in range(num_layers):
        layer_nodes.append(list(range(current_node, current_node + nodes_per_layer)))
        current_node += nodes_per_layer

    # Connect layers with regular and shortcut edges
    for layer in range(num_layers - 1):
        for node in layer_nodes[layer]:
            # Regular edges to the next layer
            for next_node in random.sample(layer_nodes[layer + 1], k=5):
                graph[node].append(next_node)
            # Shortcut edges to nodes further ahead (1-3 layers ahead)
            if layer + 2 < num_layers:
                for shortcut_node in random.sample(layer_nodes[layer + 2], k=2):
                    graph[node].append(shortcut_node)
            if layer + 3 < num_layers:
                for shortcut_node in random.sample(layer_nodes[layer + 3], k=1):
                    graph[node].append(shortcut_node)

    # Last layer has no outgoing edges
    return graph, current_node - 1  # Return graph and the total node count

# Generate a complex large DAG
graph, n = create_large_dag()


def imprimeCaminho(ot, prox):
    # Print the longest path based on `prox` pointers
    u = ot[0]
    path = [u]
    while prox[u] != -1:
        u = prox[u]
        path.append(u)
    print("Longest Path:", path)

def ordTop(v, graph, marked, Dm, prox, ot, os, mc):
    marked[v] = True
    for w in graph.get(v, []):
        if not marked[w]:
            ordTop(w, graph, marked, Dm, prox, ot, os, mc)
        if Dm[w] + 1 > Dm[v]:  # Assumes any `w` as the optimal choice without rechecking
            Dm[v] = Dm[w] + 1
            prox[v] = w
    ot[os[0]] = v
    os[0] -= 1
    mc[0] = max(mc[0], Dm[v])

def longest_path_original(graph, n):
    marked = {i: False for i in range(1, n + 1)}
    Dm = {i: 0 for i in range(1, n + 1)}
    prox = {i: -1 for i in range(1, n + 1)}
    ot = [0] * n
    os = [n - 1]  # os is a list to hold mutable integer
    mc = [0]  # mc to store the maximum length of the longest path

    for i in range(1, n + 1):
        if not marked[i]:
            ordTop(i, graph, marked, Dm, prox, ot, os, mc)

    imprimeCaminho(ot, prox)

def ordTop_corrected(v, graph, marked, Dm, prox, ot, os, mc):
    marked[v] = True
    for w in graph.get(v, []):
        if not marked[w]:
            ordTop_corrected(w, graph, marked, Dm, prox, ot, os, mc)
        # Check if this path provides a greater distance before updating
        if Dm[w] + 1 > Dm[v]:
            Dm[v] = Dm[w] + 1
            prox[v] = w
    ot[os[0]] = v
    os[0] -= 1
    mc[0] = max(mc[0], Dm[v])

def longest_path_corrected(graph, n):
    marked = {i: False for i in range(1, n + 1)}
    Dm = {i: 0 for i in range(1, n + 1)}
    prox = {i: -1 for i in range(1, n + 1)}
    ot = [0] * n
    os = [n - 1]
    mc = [0]

    for i in range(1, n + 1):
        if not marked[i]:
            ordTop_corrected(i, graph, marked, Dm, prox, ot, os, mc)

    imprimeCaminho(ot, prox)

print("Original Longest Path:")
longest_path_original(graph, n)

print("\nCorrected Longest Path:")
longest_path_corrected(graph, n)
