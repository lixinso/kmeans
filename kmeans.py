import os
import math
import random

#Clustering Iris data

def read_data():
    records = []
    with open("./iris.data") as f:
        for line in f:
            record = []
            columns = line.strip().split(",")
            if(len(columns) < 5):
                continue

            sepal_length = float(columns[0])
            sepal_width = float(columns[1])
            petal_length = float(columns[2])
            petal_width = float(columns[3])
            classification = columns[4]
            record = [sepal_length, sepal_width, petal_length, petal_width, classification]
            #print(record)
            records.append(record)

    random.shuffle(records)
    return records

def init_centroid(records,n):
    centroids = []
    len_records = len(records)
    split = (int)(len_records / n)
    for i in range(n):
        r = records[i*split + (int)(split / 2)]
        centroids.append(r)
    return centroids

def distance(record1, record2):
    dis = math.sqrt(math.pow(record1[0] - record2[0], 2) + math.pow(record1[1] - record2[1], 2) + math.pow(record1[2] - record2[2], 2) + math.pow(record1[3] - record2[3], 2))
    return dis

def clustering(records,n):
    #init centroid
    centroids = init_centroid(records,n)
    clusters = [] # [[idx11,idx12,idx13...],...,[idx21,idx22,idx23...]]
    for i in range(n):
        clusters.append([])

    #
    iteration = 0
    error = 999999
    while(error > 1 and iteration < 10):

        clusters = []  # [[idx11,idx12,idx13...],...,[idx21,idx22,idx23...]]
        for i in range(n):
            clusters.append([])

        #assign each record to centroid/class
        total_distance = 0
        for idx, record in enumerate(records):
            min_distance = 9999
            cluster_idx = -1
            for i in range(n):
                dis = distance(record, centroids[i])
                if dis < min_distance:
                    min_distance = dis
                    cluster_idx = i
            clusters[cluster_idx].append(idx)
            total_distance += min_distance

        #calculate the error

        #calculate new centroid
        centroids = []
        for i in range(n):
            cluster = clusters[i]
            centroid_new = [0, 0, 0, 0]
            for ii in cluster:
                r_ii = records[ii]
                centroid_new[0] += r_ii[0]
                centroid_new[1] += r_ii[1]
                centroid_new[2] += r_ii[2]
                centroid_new[3] += r_ii[3]

            if len(cluster) > 0:
                centroid_new[0] = centroid_new[0] / len(cluster)
                centroid_new[1] = centroid_new[1] / len(cluster)
                centroid_new[2] = centroid_new[2] / len(cluster)
                centroid_new[3] = centroid_new[3] / len(cluster)

            centroids.append(centroid_new)

        iteration += 1


    for idx, cluster in enumerate(clusters):
        print("cluster: " , idx, cluster)
        for c in cluster:
            print(records[c][4] + "\t")

recs = read_data()
clustering(recs,3)

