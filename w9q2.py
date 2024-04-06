data = [200, 300, 400, 600, 1000]

min_val = min(data)
max_val = max(data)

normalized_data = [(x - min_val) / (max_val - min_val) for x in data]

print(normalized_data)