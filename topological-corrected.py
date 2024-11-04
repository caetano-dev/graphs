from collections import deque, defaultdict


graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5, 6],
    4: [7],
    5: [7, 8],
    6: [8],
    7: [9],
    8: [9],
    9: [10],
    10: []
}

def topological_sort_corrected(graph):
    # Calculate in-degrees for all nodes
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize the queue with nodes having in-degree 0
    q = deque([node for node in in_degree if in_degree[node] == 0])
    ordering = []
    visited = set(q)  # Track nodes already added to avoid duplicates

    while q:
        v = q[0]  # Get the front element
        ordering.append(v)
        for w in graph[v]:
            in_degree[w] -= 1
            if in_degree[w] == 0 and w not in visited:
                q.append(w)
                visited.add(w)  # Mark as added
        q.popleft()  # Remove the front element

    return ordering


def topological_sort_original(graph):
    # Calculate in-degrees for all nodes
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize the queue with nodes having in-degree 0
    q = deque([node for node in in_degree if in_degree[node] == 0])
    ordering = []

    while q:
        v = q[0]  # Get the front element
        ordering.append(v)
        for w in graph[v]:
            in_degree[w] -= 1
            if in_degree[w] == 0:
                q.append(w)
        q.popleft()  # Remove the front element

    return ordering

# Original topological sort
print("Original Topological Sort:", topological_sort_original(graph))

# Corrected topological sort
print("Corrected Topological Sort:", topological_sort_corrected(graph))
