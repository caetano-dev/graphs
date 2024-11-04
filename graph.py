
def generate_grid_graph(p, q):
    # Number of vertices in the graph
    num_vertices = p * q

    # Initialize an adjacency matrix with zeros
    adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]


    # Iterate through each vertex in the grid
    for row in range(q):
        for col in range(p):
            current_node = row * p + col

            # Connect to the node on the right (if it exists)
            if col < p - 1:
                right_node = current_node + 1
                adjacency_matrix[current_node][right_node] = 1
                adjacency_matrix[right_node][current_node] = 1

            # Connect to the node below (if it exists)
            if row < q - 1:
                bottom_node = current_node + p
                adjacency_matrix[current_node][bottom_node] = 1
                adjacency_matrix[bottom_node][current_node] = 1

    return adjacency_matrix

# Example of how to use the function
p = int(input("Enter the number of columns: "))
q = int(input("Enter the number of lines: "))
adj_matrix = generate_grid_graph(p, q)

# Print the adjacency matrix
for row in adj_matrix:
    print(row)
