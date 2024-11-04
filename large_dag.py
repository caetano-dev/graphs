
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
