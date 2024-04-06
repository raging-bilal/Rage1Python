import math

def euclidean_distance(tuple1, tuple2):
    
    squared_diff_sum = sum([(x - y) ** 2 for x, y in zip(tuple1, tuple2)])

    distance = math.sqrt(squared_diff_sum)
    return distance

tuple1 = (22, 1, 42, 10)
tuple2 = (20, 0, 36, 8)
distance = euclidean_distance(tuple1, tuple2)
print("The Euclidean distance between", tuple1, "and", tuple2, "is:", distance)
