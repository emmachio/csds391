import math
import collections
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

csvFile = 'irisdata.csv'
def kmeansClustering(k, dimensions, csvFile):
    objectiveFunction = []
    random.seed(2409)
    # determining when the means will converge
    converged = False
    # an array of arrays where each array element is the point's coordinates
    allDataPoints = []
    csvData = pd.read_csv(csvFile)
    data = csvData.values
    allMeans = []
    # numberOfValues being the total number of data points
    numberOfValues = len(csvData)
    # putting all the data points into one array
    for i in range(numberOfValues):
        dataPoint = []
        # if running the k-means in general, uncomment this code:
        # for n in range(dimensions):
        # if running k-means in general, comment this code:
        for n in range(2,4):
            dataPoint.append(data[i][n])
        allDataPoints.append(dataPoint)

    # the randomized means that are chosen
    updatedMeans = []
    oldMean = []
    for j in range(k):
        randomPoint = random.randint(0,numberOfValues-1)
        oldMean.append(allDataPoints[randomPoint])

    while converged == False:
        # clusters is an array that will hold the k clusters
        clusters = []
        for j in range(k):
            clusters.append([])
        # iterating through all the values
        for x in range(numberOfValues):
            distances = []
            # finding the point from each of the k values
            for m in range(k):
                distances.append(distance(oldMean[m], allDataPoints[x]))
            # finding the minimum distance and assigning the point to that cluster
            minValue = min(distances)
            minIndex = distances.index(minValue)
            clusters[minIndex].append(allDataPoints[x])
        sum = 0
        for i, cluster in enumerate(clusters):
            currentmean = np.array(oldMean[i])
            clustersArray = np.array(cluster)
            sum += np.sum(np.linalg.norm(clustersArray - currentmean, axis=1) ** 2)
        # calculating the objectiveFunction value and storing it so that it can be plotted later
        objectiveFunction.append(sum)
        # calculating the means of each cluster
        updatedMeans = updatingMean(clusters, dimensions, k)
        distances = np.linalg.norm(updatedMeans - oldMean, axis=1)
        # determining when the code has converged to a local minimum
        converged = np.all(distances < 1e-4)
        allMeans.append(oldMean)
        # updating the means to the updated means - so that the mean gets closer and closer tot the minimum
        oldMean = updatedMeans
    return allDataPoints, updatedMeans, objectiveFunction, allMeans, clusters

# helper code used to find the euclidean distance
def distance(point1, point2):
    totalValues = []
    sum = 0
    for i in range(len(point1)):
        dimensionDistance = (point1[i]-point2[i])**2
        totalValues.append(dimensionDistance)
    for j in range(len(totalValues)):
        sum = sum + totalValues[j]
    result = math.sqrt(sum)
    # print(sum)
    return result

# helper function that finds the mean for each cluster
def updatingMean(clusters, dimensions, k):
    newMeans = []
    for i in range(k):
        kClusterMeans = []
        for j in range(dimensions):
            dimensionPoints = []
            for k in range(len(clusters[i])):
                dimensionPoints.append(clusters[i][k][j])
            dimensionPoints=np.array(dimensionPoints)
            kClusterMeans.append(np.mean(dimensionPoints))
        newMeans.append(kClusterMeans)
    newMeans=np.array(newMeans)
    newMeans = np.nan_to_num(newMeans, nan=0)
    return newMeans

# function that will plot the learning curve for K=2,3
def plottingObjectiveFunction():
    KValues = [2,3]
    for k in KValues:
        x = []
        y = []
        dataPoints, means, objectiveFunction, allMeans, clusters = kmeansClustering(k, 4, csvFile)
        for j in range(len(objectiveFunction)):
            x.append(j)
            y.append(objectiveFunction[j])
        plt.plot(x,y)
        plt.title(f"k-means clustering objective function with K={k}")
        plt.ylim(0, 1500)
        plt.show()

# function that will plot the cluster center as it progress over the data
def plottingMeanPoints():
    KValues = [3]
    for k in KValues:
        x = []
        y = []
        dataPoints, means, objectiveFunction, allMeans, clusters = kmeansClustering(k, 2, csvFile)
        numberOfValues = len(dataPoints)
#     # putting all the data points into one array
        for i in range(numberOfValues):
            x.append(dataPoints[i][0])
            y.append(dataPoints[i][1])
        for j in range(len(allMeans)):
            xcors = []
            ycors = []
            plt.scatter(x,y, s=50)
            for n in range(len(allMeans[0])):
                xcors.append(allMeans[j][n][0])
                ycors.append(allMeans[j][n][1])
            plt.scatter(xcors, ycors, color='red', marker='x')
            plt.title(f"k-means clustering function with K={k} and run={j}")
            plt.ylim(0, 5)
            plt.xlim(0, 8)
            plt.xlabel("petal length (cm)")
            plt.ylabel("petal width (cm)")
            plt.show()

# function that plots the points in general as the clusters they were assigned to for K=2,3
def plottingPoints():
    KValues = [2, 3]
    colors = ["blue", "green", "purple"]
    for k in KValues:
        x = []
        y = []
        dataPoints, means, objectiveFunction, allMeans, clusters = kmeansClustering(k, 2, csvFile)
        for i in range(k):
            currentx = []
            currenty = []
            for j in range(len(clusters[i])):
                currentx.append(clusters[i][j][0])
                currenty.append(clusters[i][j][1])
            x.append(currentx)
            y.append(currenty)
        for j in range(k):
            plt.scatter(x[j], y[j], marker = 'o', color = "white", edgecolor=colors[j])
        xcors = []
        ycors = []
        for n in range(len(means)):
            xcors.append(means[n][0])
            ycors.append(means[n][1])
        plt.scatter(xcors, ycors, color='red', marker='x')
        # if k == 3:
        #     # marking the boundaries on the plot
        #     plt.plot([5.0,8], [1.0,1.0],color = "black")
        #     plt.plot([5.0,5.0], [0.2,2.5],color = "black")
        #     plt.plot([2.85,2.85], [0.2,2.5],color = "black")
        # else:
        #     plt.plot([3.15,3.15], [0.2,2.5],color = "black")
        plt.title(f"K={k} Decision Boundaries")
        plt.xlabel("petal length (cm)")
        plt.ylabel("petal width (cm)")
        plt.show()

# code used to determine the boundaries
def boundaries():
    KValues = [2,3]
    for k in KValues:
        petalLengths = []
        petalWidth = []
        dataPoints, means, objectiveFunction, allMeans, clusters = kmeansClustering(k, 2, csvFile)
        for i in range(k):
            lengths = []
            widths = []
            for j in range(len(clusters[i])):
                lengths.append(clusters[i][j][0])
                widths.append(clusters[i][j][1])
            petalLengths.append(lengths)
            petalWidth.append(widths)
            petalLengths[i] = collections.Counter(petalLengths[i])
            petalWidth[i] = collections.Counter(petalWidth[i])
        for i in range(k-1):
            for key in petalLengths[i]:
                if key in petalLengths[i+1]:
                    print(petalLengths[i][key], key)
                    print(petalLengths[i+1][key], key)
                    if petalLengths[i][key] == petalLengths[i+1][key]:
                        print("length", key)
        for i in range(k-1):
            for key in petalWidth[i]:
                if key in petalWidth[i+1]:
                    if petalWidth[i][key] == petalWidth[i+1][key]:
                        print("width", key)

# plottingMeanPoints()
plottingPoints()