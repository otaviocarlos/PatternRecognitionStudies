import numpy as np
import csv
import random

from settings import *
from scipy import stats
from distances import Dist
from confusion_matrix import ConfusionMatrix

class KNN():
    def __init__(self,data, answer, k = 5):
        self.df = data
        self.answer = answer
        self.k = k
        self.names = list(self.df.columns)

    def getKNN(self, data):
        distP2P = [] # list to calculate the position from data to every entry in df
        res = [] # list to return the results of the knn

        # calculating distances
        for i in range(len(self.df)):
            # distP2P = [ (distancia, index) ] 
            p1 = np.array(list(self.df.iloc[i]))

            distP2P.append( (Dist.euclid(p1, data), i) ) 
        
        # sorting distP2P
        distP2P = sorted(distP2P)
        
        for i in range(self.k):
            index = distP2P[i][1]
            res.append(index)
        
        return self.answer.loc[res]

    def createConfMatrix(self, iterations = 100):
        if iterations > len(self.df):
            raise Exception('More iterations than data')

        dim = self.answer.max()
        cm = ConfusionMatrix(dim)

        for i in range(iterations):

            # copy original data
            df = self.df
            ans = self.answer

            # select data
            item = df.loc[i]
            real = ans.loc[i]
            
            # remove data
            self.df = self.df.drop(i, axis = 0)
            self.answer = self.answer.drop(i)
            
            # get knn
            predict = self.getKNN(item)
            
            # check validation
            cm.validate(predict, real)

            # restore data
            self.df = df
            self.answer = ans
            print('loading: {}/{}'.format(i+1, iterations))
        
        print('')

        cm.showMatrix()
        print("Erro: ",cm.totalError(iterations))

            


'''

def getDistMatrix(data):
    dim = len(data)
    # creating dist matrix
    matrix = np.zeros([dim,dim])

    # calculating the distance from the superior part of the matrix
    for i in range(dim):
        for j in range(i,dim): 
            matrix[i][j] = dist(data[i],data[j])
            matrix[j][i] = matrix[i][j]

    return matrix




def main():
    # opening data
    data = []
    rank = []
    gameId = []
    rankPredict = []

    randomIndex = contPlayer
    playerData = data[randomIndex]
    playerId = gameId[randomIndex]
    playerRank = rank[randomIndex]
    del data[randomIndex] # removing random player

    # distMatrix = getDistMatrix(data)

    predict = getKNN(data, playerData, neib)

    if DEBUG: print("Player Selected: ", playerId)
    if DEBUG: print("\n{}-NN (from most similar to less similar): ".format(len(predict)))

    for i in range(len(predict)):
        if DEBUG: print("{}".format(rank[predict[i]]))
        rankPredict.append(rank[predict[i]])

    if DEBUG: print("\nPlayer's real rank: {}\n".format(playerRank))
    if DEBUG: print("---------------------------------------------")

    updateConfMatrix(playerRank, rankPredict) 


def teste():
    
    while contPlayer < epochs:
        print("Epoch: ",contPlayer,"\nTotal: ",epochs)
        print("---------------------------------------------")
        main()
        contPlayer += 1

    f = open("confusionMatrix-{}NN-results-{}-interactions.txt".format(neib,epochs),"w+")

    f.write("\nConfusion Matrix (real x predict): \n")
    f.write("   1  2  3  4  5  6  7  8\n")

    for cont, row in enumerate(confMatrix):
        f.write("{} {}\n".format(cont+1,row))

    f.close()

    print(confMatrix)

    print("Erro:",1 - totalError(),"\nAcerto: ", totalError())

    print("Done")
'''