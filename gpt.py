from itertools import permutations
from copy import deepcopy
import itertools

# Original graph definition
graph = {
    1: [3, 2],
    2: [],
    3: [5],
    4: [2],
    5: [6, 2, 4],
    6: []
}

def topological_sort(graph):
    """Deterministic topological sort algorithm (Kahn's algorithm)."""
    q = []
    topological_order = []
    indegree = {v: 0 for v in graph}

    # Calculate the indegree of each vertex
    for v in graph:
        for w in graph[v]:
            indegree[w] += 1

    # Enqueue vertices with no incoming edges
    for v in indegree:
        if indegree[v] == 0:
            q.append(v)

    # Perform topological sort
    while q:
        v = q.pop(0)
        topological_order.append(v)
        for w in graph.get(v, []):
            indegree[w] -= 1
            if indegree[w] == 0:
                q.append(w)

    return topological_order

def is_valid_topological_sort(order, graph):
    """Check if a given order is a valid topological sort."""
    position = {vertex: i for i, vertex in enumerate(order)}

    for vertex in graph:
        for neighbor in graph[vertex]:
            if position[vertex] > position[neighbor]:
                return False
    return True

def get_all_valid_topological_sorts(graph):
    """Generate all valid topological sorts for the graph."""
    vertices = list(graph.keys())
    valid_sorts = []

    # Try all possible permutations
    for perm in permutations(vertices):
        if is_valid_topological_sort(perm, graph):
            valid_sorts.append(list(perm))

    return valid_sorts

def get_algorithm_possible_outputs(graph):
    """Get all possible outputs from the original algorithm with different graph variations."""
    # Generate all possible orderings of the adjacency lists
    all_possible_outputs = set()  # To avoid duplicates

    # Generate all possible orders for the adjacency list of each node
    graph_variations = []
    for node, neighbors in graph.items():
        graph_variations.append(list(itertools.permutations(neighbors)))

    # Iterate over all combinations of permutations of adjacency lists
    for variation in itertools.product(*graph_variations):
        # Create a new graph with this specific adjacency list order
        new_graph = deepcopy(graph)
        for i, node in enumerate(graph):
            new_graph[node] = list(variation[i])

        # Run the topological sort and store the result
        sorted_output = topological_sort(new_graph)
        all_possible_outputs.add(tuple(sorted_output))

    return list(map(list, all_possible_outputs))  # Convert back to list of lists

def find_impossible_sortings(graph):
    """Find all valid topological sorts that the original algorithm cannot produce."""
    all_valid_sorts = get_all_valid_topological_sorts(graph)
    possible_outputs = get_algorithm_possible_outputs(graph)

    # Find sorts that are valid but not produced by any variation of the algorithm
    impossible_sorts = [sort for sort in all_valid_sorts if sort not in possible_outputs]

    return possible_outputs, impossible_sorts

# Test the function
possible_sorts, impossible_sorts = find_impossible_sortings(graph)

# Print the results
print("All possible topological sorts produced by the algorithm with different graph variations:")
for sort in possible_sorts:
    print(sort)

print(f"\nFound {len(impossible_sorts)} impossible sortings:")
for sort in impossible_sorts:
    print(sort)
