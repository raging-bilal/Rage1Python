def mn_dist(tuple1, tuple2):
    distance = 0
    for i in range(len(tuple1)):
        distance += abs(tuple1[i] - tuple2[i])
    return distance
    
print(mn_dist(tuple1=(22, 1, 42, 10) ,tuple2=(20, 0, 36, 8)))