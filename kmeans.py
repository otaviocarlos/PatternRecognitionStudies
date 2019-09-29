from settings import *
from distances import Dist
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np
import random

# FIXME: column names are defined to be 'x' and 'y' -> only 2D data is accepted.
# TODO: set standard names to N columns
# TODO: create a stop condition: 
#       a   = acceptance point
#       clp = centroids las pos
#       cnp = centroids new pos
#       if cnp - clp < a , stop the algorithm

class K_means():
    def __init__(self, data, k = 3, alpha = 0.05):
        if not isinstance(data, pd.DataFrame):
            raise Exception("data is not a pandas DataFrame instance")

        self.df = data
        self.k = k
        self.dim = self.df.shape # returns (nrows, ncols)
        self.names = list(self.df.columns)
        self.centroids = [ Centroids(alpha) for i in range(k) ]
        self.colors = self.initColors(self.k)
        self.running = False

        if DEBUG: self.plot(main = 'before')
        
        self.initGroups()

    def initColors(self,k):
        cmap = plt.get_cmap('Set1') # using a map of colours
        color = [cmap(i) for i in range(k)]
        keys = [i for i in range(len(color))]
        return dict(zip(keys, color))

    def update(self, iterations = None):
        # loop to update
        if (iterations == None):
            cont = 0
            self.running = True
            while self.running:
                cont += 1
                if DEBUG: self.plot()
                means = self.calculateMean()
                self.updateCentroidsPos(means)
                self.updateGroups()
                print("iteration: ", cont)

        else: 
            for i in range(iterations):
                if DEBUG: self.plot()
                means = self.calculateMean()
                self.updateCentroidsPos(means)
                self.updateGroups()
                print("iteration {}/{}".format(i+1,iterations))

        print('Done')

    def initGroups(self):
        groups = []
        # setting centroids colors:
        vocabulary = [ i for i in range(self.k) ]
        for count,c in enumerate(self.centroids):
            c.color = self.colors.get(vocabulary[count], 'black')

        # calculate the distance for data samples to each centroid, setting each group
        for i in range(self.dim[0]):
            dist = []
            for c in range(self.k):
                p1 = self.df.loc[i,:]
                p2 = np.array(list(self.centroids[c].getPos()))
                dist.append(Dist.euclid(p1, p2))
            
            # nearest centroid
            nc = dist.index(min(dist))
            groups.append(nc)

        # add a new column to df representing each group
        self.df['group'] = groups  

    def updateGroups(self):
        groups = []
        # calculate the distance of data samples to each centroid, setting each group
        for i in range(self.dim[0]):
            dist = []
            for c in range(self.k):
                p1 = self.df.loc[i, self.names]
                p2 = np.array(list(self.centroids[c].getPos()))
                dist.append(Dist.euclid(p1, p2))

            # nearest centroid
            nc = dist.index(min(dist))
            self.df.at[i, 'group'] = nc


    def calculateMean(self):
        # calculating mean
        groups = self.df.groupby('group')
        return groups.mean()
        
    def updateCentroidsPos(self, means):
        # TODO: when in N dimensions, use a second for loop to run 
        #       throug a array of "positions"
        isFixed = []
        for count, c in enumerate(self.centroids):
            try:
                # setting the new centroids positions:
                c.updateLastPos()
                c.x = means.at[count,'x']
                c.y = means.at[count,'y']
                isFixed.append(c.checkMovement())

            except:
                pass
        
        # checking if all centroids are moving significantly
        self.checkFixed(isFixed)

    def checkFixed(self, isFixed):
        s = 0
        for i in range(len(isFixed)):
            if isFixed[i] == True:
                s += 1

        if s == len(isFixed):
            self.running = False


    def plot(self, main = 'Plot'):
        # TODO: plot the figure with title given by the arg 'main'
        # closing previous plots
        # plt.close()
        
        # plot points in a scatter plot
        try:
            for i in range(len(self.df)):
                plt.scatter(self.df.at[i,'x'],self.df.at[i,'y'] , color = self.colors.get(self.df.at[i,'group'], 'black'))
        except:
            for i in range(len(self.df)):
                plt.scatter(self.df.at[i,'x'],self.df.at[i,'y'] , color = 'black')
        

        # plot centroids
        if SHOW_CENTROIDS:
            ax = plt.gca()
            for c in self.centroids:
                rect = patches.Circle(c.getPos(), radius = 0.02, facecolor = c.color, edgecolor = 'black', fill = True )
                ax.add_patch(rect)

        plt.show()

class Centroids():
    def __init__(self, alpha):
        # TODO: adjust the 2D centroid to fit in N dimensions
        self.x = random.random()
        self.y = random.random()
        self.lastPos = None
        self.color = 'r'
        self.alpha = alpha

    def getPos(self):
        return (self.x, self.y)

    def updateLastPos(self):
        self.lastPos = np.array([self.x,self.y])

    def checkMovement(self):
        newPos = np.array([self.x,self.y])
        dif = True if (Dist.euclid(newPos,self.lastPos)) < self.alpha else False 
        return dif

