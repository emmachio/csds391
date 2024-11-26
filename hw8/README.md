Problem 5:
a:
	The code for that can be found in the kmeansClustering method which intakes the csv file, k (number of clusters), and dimensions. However, since it was also used in the cases where we were specifically looking at petal length and width, there is a section that needs to be commented out to be able to deal with an arbitrary number of dimensions.
b:
	While the code for calculating the objective function is in the kmeansClustering method, the actual method that plots out this learning curve is plottingObjectiveFunction.
c. 
	The code that collects all the different cluster means is the kmeansCLustering method as it saves the previous clustering mean before updating. However, the function to plot it is plottingMeanPoints.

d. 
	In order to find the boundaries, the function boundaries is there to find it. However, the code that draws the boundary line is in the plotPoints function which also plots the data points accordingly to their cluster.