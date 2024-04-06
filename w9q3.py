R = [(1, 2), (2, 3), (3, 4), (4, 5)]

R_inv = [(y, x) for (x, y) in R]

U = set(range(1, 6)) 
R_comp = [(x, y) for x in U for y in U if (x, y) not in R]

# Print the results
print("R =", R)
print("Inverse of R =", R_inv)
print("Complement of R =", R_comp)