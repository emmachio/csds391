import math
import collections
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as random

def sigmoid(x):
    return 1/(1+np.exp(-x))

csvFile = 'irisdata.csv'
colors = ["blue", "green"]
csvData = pd.read_csv(csvFile)
data = csvData.values
allData = []
petalLengths = []
petalWidths = []
cvalues = []
for i in range(len(data)):
    if data[i][4] == 'versicolor' or data[i][4] == 'virginica':
        current = []
        petalLengths.append(data[i][2])
        petalWidths.append(data[i][3])
        current.append(data[i][2])
        current.append(data[i][3])
        allData.append(current)
        if data[i][4] == 'versicolor' :
            cvalues.append(0)
        elif data[i][4] == 'virginica':
            cvalues.append(1)
petalLengths = np.array(petalLengths)
petalWidths = np.array(petalWidths)
xvalues=[[],[]]
yvalues=[[],[]]

def oneLayerNN(weights):
    # x = np.linspace(3,7,100)
    # y = np.linspace(0,3,100)
    x = petalLengths
    y = petalWidths
    z = []
    for i in range(len(x)):
        X = x[i]
        Y = y[i]
        result = sigmoid(weights[0]*X+weights[1]*Y+weights[2])
        z.append(result)
    return z
# print(oneLayerNN([0.87,0.93,-5.7]))

# print(oneLayerNN())
def decisionBoundary(weights, error):
    colors = ["blue", "green"]
    for i in range(len(data)):
        # adding values to x and y array for graphing
        if data[i][4] == 'versicolor':
            xvalues[0].append(data[i][2])
            yvalues[0].append(data[i][3])
        if data[i][4] == 'virginica':
            xvalues[1].append(data[i][2])
            yvalues[1].append(data[i][3])
    # plotting x and y scatter points
    for j in range(len(colors)):
        plt.scatter(xvalues[j], yvalues[j], marker = 'o', color = "white", edgecolor=colors[j])
    plt.title(f"Petal Length v. Width (decision boundary)")
    # given an array of list, draw the boundary
    for i in range(len(weights)):
        x1 = np.linspace(3.0, 8.0, 100)
        x2 = -(weights[i][0] * x1 + weights[i][2]) / weights[i][1]
        plt.plot(x1, x2, label="Decision Boundary", color="red")
    plt.xlabel("petal length (cm)")
    plt.ylabel("petal width (cm)")
    plt.xlim(petalLengths.min()-0.5, petalLengths.max()+0.5)
    plt.ylim(petalWidths.min()-0.5, petalWidths.max()+0.5)
    plt.show()
# decisionBoundary([[0.87,0.93,-5.7]])

def classifier(points, weights):
    # print(sigmoid(weights[0]*points[0]+weights[1]*points[1]+weights[2]))
    for i in range(2):
        if sigmoid(weights[0]*points[0]+weights[1]*points[1]+weights[2]) < 0.5:
            return 0
        else:
            return 1

def examples():
    colors = ["green", "blue"]
    # example points such that the first two are versicolor, the next two are virginica,
    # and the next two are on the boundary such that the point is 0 and the second point 1
    examplePoints = [[3.5,1], [3.9,1.1], [6.9,2.3], [6.4,2],[4.9,1.5],[5,1.5]]
    xvalues = [[],[]]
    yvalues = [[],[]]
    weights = [0.87,0.93,-5.7]
    for i in range(len(examplePoints)):
        if classifier(examplePoints[i], weights) == 0:
            xvalues[0].append(examplePoints[i][0])
            yvalues[0].append(examplePoints[i][1])
        else:
            xvalues[1].append(examplePoints[i][0])
            yvalues[1].append(examplePoints[i][1])
    for j in range(len(colors)):
        plt.scatter(xvalues[j], yvalues[j], marker = 'o', color = "white", edgecolor=colors[j])
    for i in range(len(weights)):
        x1 = np.linspace(3.0, 8.0, 100)
        x2 = -(weights[0] * x1 + weights[2]) / weights[1]
        plt.plot(x1, x2, label="Decision Boundary", color="red")
    plt.title("Petal Length v. Width (examples)")
    plt.xlabel("petal length (cm)")
    plt.ylabel("petal width (cm)")
    plt.show()
# examples()

def threeDPlotting():
    x = np.linspace(3,7,100)
    y = np.linspace(0,3,100)
    # x = petalLengths
    # y = petalWidths
    X,Y = np.meshgrid(x,y)
    # since the boundaries within the actual classifier code made it so that the plot was incredibly
    # focused on one portion, making it a straight line, by changing the bias, the
    # learning curve can be seen signficiantly more
    z = 0.87*X+0.93*Y-5.7
    Z = sigmoid(z)
    # Z = oneLayerNN()
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    surface = ax.plot_surface(X,Y,Z, cmap='viridis', edgecolor='none')
    ax.set_xlim(3,7)
    ax.set_ylim(0,3)
    ax.set_zlim(0,1)
    ax.set_xlabel("petal length (cm)")
    ax.set_ylabel("petal width (cm)")
    ax.set_zlabel("neural network")
    ax.view_init(azim=120)
    ax.set_title("neural network output 3d surface plot")
    plt.show()


def originalData():
    colors = ["blue", "green"]
    csvData = pd.read_csv(csvFile)
    data = csvData.values
    xvalues=[[],[]]
    yvalues=[[],[]]
    for i in range(len(data)):
        if data[i][4] == 'versicolor':
            xvalues[0].append(data[i][2])
            yvalues[0].append(data[i][3])
        if data[i][4] == 'virginica':
            xvalues[1].append(data[i][2])
            yvalues[1].append(data[i][3])
    for j in range(len(colors)):
        plt.scatter(xvalues[j], yvalues[j], marker = 'o', color = "white", edgecolor=colors[j])
    plt.title("Petal Length v. Width (original)")
    plt.xlabel("petal length (cm)")
    plt.ylabel("petal width (cm)")
    plt.show()
# originalData()

def error(dataVectors, parameters, patternVector):
    sum = 0
    dataVectors = np.array(dataVectors)
    parameters = np.array(parameters)
    patternVector = np.array(patternVector)
    differences = []
    product = oneLayerNN(parameters)
    # for i in range(len(dataVectors)):
    #     product.append(parameters[0]*dataVectors[i][0] + parameters[1]*dataVectors[i][1]+parameters[2])
    difference = product - patternVector
    difference = (difference)**2
    sum = difference.sum()
    return sum/len(dataVectors)
# print(error(allData, [0.87,0.93,-5.7], cvalues))
# print(error(allData, [0.2,0.2,-2], cvalues))
# decisionBoundary([[0.87,0.93,-5.7], [0.2,0.2,-2]])


def gradient(dataVectors, parameters, patternVector, epsilon):
    sum = 0
    N = len(dataVectors)
    # epsilon = 0.0001
    dataVectors = np.array(dataVectors)
    parameters = np.array(parameters)
    patternVector = np.array(patternVector)
    values = []
    product = oneLayerNN(parameters)
    product = np.array(product)
    currentWeight = [[],[],[]]
    # iterating through all the vector values and multiplying by the function
    for i in range(len(product)):
        current = (product - patternVector)*(product)*(1-product)
        currentWeight[0].append(current * dataVectors[i][0])
        currentWeight[1].append(current * dataVectors[i][1])
        currentWeight[2].append(current)
    currentWeight[0] = np.array(currentWeight[0])
    currentWeight[1] = np.array(currentWeight[1])
    currentWeight[2] = np.array(currentWeight[2])
    # summing all the values and multiplying it by 2/N
    gradient1 = (currentWeight[0].sum() * 2)/N
    gradient2 = (currentWeight[1].sum() * 2)/N
    biasgradient = (currentWeight[2].sum() * 2)/N
    # print(gradient1, gradient2, biasgradient)
    # setting the new weights to be w_t+1 = w_t - epsilon*gradientWeight
    parameters[0] = parameters[0] - (epsilon*gradient1)
    parameters[1] = parameters[1] - (epsilon*gradient2)
    parameters[2] = parameters[2] - (epsilon*biasgradient)
    return parameters
gradient(allData, [0.87, 0.93, -5.7], cvalues, 0.001)
# decisionBoundary([[0.2,0.2,-2], [0.241, 0.214, -1.99]])

def optimizeGradient(dataVectors, weight, patternVectors, epsilon, convergence):
    converge = False
    weights = []
    errors = []
    # errors.append(error(dataVectors, weight, patternVectors))
    while not converge:
        weight = gradient(dataVectors, weight, patternVectors, epsilon)
        weights.append(weight)
        if error(dataVectors, weight, patternVectors) < convergence:
            converge = True
        errors.append(error(dataVectors, weight, patternVectors))
        print(error(dataVectors, weight, patternVectors))
        # print(weight)
    return weights, errors
# optimizeGradient(allData, [0.2,0.2,-2], cvalues)
def showoptimization(dataVectors, weight, patternVectors, epsilon, convergence):
    weights, errors = optimizeGradient(dataVectors, weight, patternVectors, epsilon, convergence)
    x = []
    y = []
    for i in range(len(weights)):
        x.append(i)
        y.append(errors[i])
        # if(errors[i] < errors[0]/2):
        decisionBoundary([weights[i]], errors[i])
    plt.plot(x, y)
    plt.xlabel("iterations")
    plt.ylabel("MSE")
    plt.title(f"Error Learning Curve with Epsilon {epsilon}")
    plt.show()

weights = [0.2,0.6,-5]
# weights = [[0.32936788, 0.2782586,  0.29833139]]
# for i in range(5):
#     weights.append(gradient(allData, weights[i], cvalues))
# decisionBoundary(weights)
random.seed(600)
random1 = random.uniform(0.2, 1)
random2 = random.uniform(0.2, 1)
random3 = random.uniform(-6, 0)
# print(random1, random2, random3)
randomArray = [random1, random2, random3]
# showoptimization(allData, randomArray, cvalues, 0.001, 0.1517)
# showoptimization(allData, randomArray, cvalues, 0.005, 0.152)
# decisionBoundary([randomArray], 0.001)
print(error(allData, [0.2,0.2,-2], cvalues))