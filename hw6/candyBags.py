import matplotlib.pyplot as plt

# function to calculate Bayesian learning
def candyBags(flavors, ratios, probabilities, candyOrder):
    # an array to keep track of all the probabilities for the plot
    allProbabilities = []
    # putting in the prior probabilities to begin with
    for i in range(len(probabilities)):
        current = []
        current.append(probabilities[i])
        allProbabilities.append(current)
        # determining which candy type was picked out first
    candy = candyOrder[0]
    # finding the index of that candy
    candyIndex = flavors.index(candy)
    # keeping track of all the P(d|h_i)
    Pdhlist = []
    # putting in the first values as an array
    for i in range(len(ratios)):
        current = []
        current.append(ratios[i][candyIndex])
        Pdhlist.append(current)
    # looping it per number of candies
    for i in range(len(candyOrder)):
        # since the first ratios have already been put in, only do this step when its after the first round
        if i >= 1:
            candy = candyOrder[i]
            candyIndex = flavors.index(candy)
            for i in range(len(ratios)):
                current = Pdhlist[i]
                current.append(ratios[i][candyIndex])
                Pdhlist[i] = current
        # keeping track of the sum for alpha
        sum = 0
        # for each of the bags
        for j in range(len(probabilities)):
            # find the current probability of the bag - P(h_i)
            Phi = probabilities[j]
            # find P(d|h_i) by multiplying all the previous probabilities
            Pdhi = Pdh(Pdhlist[j])
            # find P(d|h_i) * P(h_i)
            probabilities[j] = Pdhi*Phi
            sum = sum + probabilities[j]
        # normalize all the values by putting it over the sum
        for j in range(len(probabilities)):
            Phi = probabilities[j]
            probabilities[j] = Phi/sum
            if i >= 1:
                allProbabilities[j].append(probabilities[j])
    # for i in range(len(probabilities)):
    return probabilities, allProbabilities

def Pdh(priorPdh):
    result = priorPdh[0]
    for i in range(1, len(priorPdh)):
        result = result * priorPdh[i]
    return result

def plotBags(numberofCandies, allProbabilities):
    x = []
    for i in range(numberofCandies):
        x.append(i)
    for i in range(len(allProbabilities)):
        label = "P(h_"+str(i+1)+"| d)"
        plt.plot(x, allProbabilities[i], label = label, marker='o')
    plt.xlabel("number of candies")
    plt.ylabel("probability")
    plt.title("probability per bag")
    plt.legend()
    plt.show()

# input the flavors as a list of strings ex: ["cherry", "lime"]
flavors = ["cherry", "lime"]
# input the ratios as a list of a list in the same order as the flavors were given ex: [[1,0],[0.75,0.25],[0.5,0.5],[0.25,0.75],[0,1]]
ratios = [[1,0],[0.75,0.25],[0.5,0.5],[0.25,0.75],[0,1]]
# input the prior probabilites per bag as a list ex: [0.1,0.2,0.4,0.2,0.1]
priorProbabilities = [0.1,0.2,0.4,0.2,0.1]
# input the order as the candies come out ex: ["lime", "lime", "lime", "lime", "lime", "lime", "lime", "lime", "lime", "lime"]
candyOrder = ["cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry", "lime", "lime", "lime"]
# default will be the question in the textbook but can be changed
probabilities, allProbabilities = candyBags(flavors, ratios, priorProbabilities, candyOrder)
plotBags(len(candyOrder), allProbabilities)
print(probabilities)