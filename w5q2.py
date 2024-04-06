import statistics

ages = [15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

max_value = max(ages)
print("Max value:", max_value)

min_value = min(ages)
print("Min value:", min_value)

std_dev = statistics.stdev(ages)
print("Standard deviation:", std_dev)

variance = statistics.variance(ages)
print("Variance:", variance)
