from collections import defaultdict
from typing import List
# create all possible permutations of the edges of this graph
graph = {
    1: [2,3],
    2: [],
    3: [5],
    4: [2],
    5: [6,2,4],
    6: []
}


def topological_sort(graph):
    # Initialize a queue to keep track of vertices with no incoming edges
    q = []
    # Initialize a list to keep track of the topological order
    topological_order = []
    # Initialize a dictionary to keep track of the indegree of each vertex
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

print(topological_sort(graph))
