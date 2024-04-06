data = [200, 300, 400, 600, 1000]

mean = sum(data) / len(data)

variance = sum((x - mean) ** 2 for x in data) / len(data)
stdev = variance ** 0.5

# Calculate the z-score normalization of the data
z_scores = [(x - mean) / stdev for x in data]

print("Original data:", data)
print("Z-score normalization:", z_scores)
