import statistics

ages = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

mean_age = statistics.mean(ages)
print("Mean age:", mean_age)

median_age = statistics.median(ages)
print("Median age:", median_age)

mode_age = statistics.mode(ages)
print("Mode is:", mode_age)

q1 = statistics.median(filter(lambda x: x < median_age, ages))
print("First quartile (Q1):", q1)

q3 = statistics.median(filter(lambda x: x > median_age, ages))
print("Third quartile (Q3):", q3)
