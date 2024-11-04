from collections import defaultdict
graph = {
    1: [2, 3],
    2: [],
    3: [5],
    4: [2],
    5: [2, 4, 6],
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

print("-------------------")



def all_topological_sorts(graph):
    def backtrack(path, visited, indegree):
        # If the current path includes all vertices, add it to the results
        if len(path) == len(graph):
            result.append(path[:])
            return

        # Try to add each vertex with no incoming edges to the current path
        for v in graph:
            if indegree[v] == 0 and not visited[v]:
                # Mark the vertex as visited
                visited[v] = True
                path.append(v)

                # Decrease the indegree of its neighbors
                for neighbor in graph[v]:
                    indegree[neighbor] -= 1

                # Recur with the updated path and indegree
                backtrack(path, visited, indegree)

                # Backtrack: undo the changes
                path.pop()
                visited[v] = False
                for neighbor in graph[v]:
                    indegree[neighbor] += 1

    # Initialize the result list to store all topological orders
    result = []
    # Initialize the visited dictionary to keep track of visited vertices
    visited = {v: False for v in graph}
    # Initialize the indegree dictionary to keep track of the indegree of each vertex
    indegree = {v: 0 for v in graph}

    # Calculate the indegree of each vertex
    for v in graph:
        for w in graph[v]:
            indegree[w] += 1

    # Start the backtracking process
    backtrack([], visited, indegree)

    return result

print(all_topological_sorts(graph))
