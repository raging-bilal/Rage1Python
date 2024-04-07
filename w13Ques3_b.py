import numpy as np

# define the adjacency matrix
adj_matrix = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
])

# adj_matrix = np.array([
#     [0, 1, 1, 0],
#     [1, 0, 1, 1],
#     [1, 1, 0, 0],
#     [0, 1, 0, 0]
# ])

# print the adjacency matrix
print("Adjacency Matrix:")
print(adj_matrix)

# check if the graph is complete
num_vertices = len(adj_matrix)
is_complete = True

for i in range(num_vertices):
    for j in range(num_vertices):
        if i != j and adj_matrix[i][j] != 1:
            is_complete = False

if is_complete:
    print("The graph is complete.")
else:
    print("The graph is not complete.")
