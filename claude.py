from itertools import permutations

graph = {
    1: [3,2],
    2: [],
    3: [5],
    4: [2],
    5: [2,4,6],
    6: []
}

from itertools import permutations

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
    """Get all possible outputs from the original algorithm."""
    return [topological_sort(graph)]

def find_impossible_sortings(graph):
    """Find all valid topological sorts that the original algorithm cannot produce."""
    all_valid = get_all_valid_topological_sorts(graph)
    algorithm_outputs = get_algorithm_possible_outputs(graph)

    # Since the algorithm is deterministic, we only compare against its single output
    possible_sort = algorithm_outputs[0]

    # Find sorts that are valid but not produced by the algorithm
    impossible = [sort for sort in all_valid if sort != possible_sort]

    return possible_sort, impossible

# Test the function
possible_sort, impossible_sorts = find_impossible_sortings(graph)

# Print the results
print("Normal topological sort produced by the algorithm:")
print(possible_sort)

print(f"\nFound {len(impossible_sorts)} impossible sortings:")
for sort in impossible_sorts:
    print(sort)
