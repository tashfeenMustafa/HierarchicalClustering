#!/usr/bin/env python
# coding: utf-8

import math


# measure euclidean distance between two points
def euclidean_distance(centroid_1, centroid_2):
    distance = 0
    s = []

    # Looping over both centroids and calculating square of
    # each centroid_1[i] and centroid_2[i] and keeping it in 's'
    for i in range(len(centroid_1)):
        s.append((centroid_1[i] - centroid_2[i]) ** 2)

    sum_of_s = 0
    # Adding all numbers in 's'
    for i, num in enumerate(s):
        sum_of_s += num

    # Then square rooting the sum of 's' to find distance
    distance = math.sqrt(sum_of_s)
    return distance


# calculate centroid given two points
def calculate_centroid(point_1, point_2):
    # initialize new centroid
    new_centroid = []

    # appenind addition of each point_1[i] and point_2[j]
    for i in range(len(point_1)):
        new_centroid.append((point_1[i] + point_2[i]))

    # finding the average for each point
    for i in range(len(new_centroid)):
        new_centroid[i] = new_centroid[i] / 2

    return new_centroid


# loading and processing data
file = open('hierarchicalClusterData.csv')
data = []
for line in file:
    line = line.strip().split(',')
    data.append(line)

for i in range(len(data)):
    for j in range(len(data[i])):
        if i != 0:
            data[i][j] = float(data[i][j])

# discaring the top row of data as top row contains only feature names
data = data[1:]

# Initializing
# Considering all points to be clusters with their vectors as centroids
# Initially each point is a cluster. The clusters will be represented using their index in data

# Using proximity matrix to keep track of distance between centroids
proximity_matrix = [[0 for _ in range(len(data))] for _ in range(len(data))]
centroids = data

count = 1
while len(centroids) > 3:
    print('count: ', count)

    # Step 1: take each cluster and measure the distance between all the other clusters.   
    for i, point_i in enumerate(centroids):
        for j, point_j in enumerate(centroids):
            distance = euclidean_distance(point_i, point_j)
            # update distance in proximity matrix
            proximity_matrix[i][j] = distance

    # Step 2: Merge the points with the smallest distance in the proximity matrix
    #         And then update the new centroids
    min_distance = 1000.0
    centroid_index_i = None
    centroid_index_j = None

    for i in range(len(proximity_matrix)):
        for j in range(len(proximity_matrix[i])):
            if proximity_matrix[i][j] <= min_distance and proximity_matrix[i][j] > 0:
                min_distance = proximity_matrix[i][j]
                centroid_index_i = i
                centroid_index_j = j
    print(centroid_index_i, centroid_index_j)

    x1 = [centroid_index_i, proximity_matrix[i][j]]
    y1 = [centroid_index_i, proximity_matrix[i][j]]

    new_centroid = calculate_centroid(centroids[centroid_index_i], centroids[centroid_index_j])
    centroids.pop(centroid_index_i)
    centroids.pop(centroid_index_j)

    centroids.append(new_centroid)
    print(centroids)

    proximity_matrix = [[0 for _ in range(len(centroids))] for _ in range(len(centroids))]
    # Step 3: go back to step 1
    # do this until you have 3 clusters
    count += 1

print(centroids)
