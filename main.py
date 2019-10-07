from kmeans import K_means
from knn import KNN

import pandas as pd
from preprocessing import PreProcessing as pp

import numpy as np
import random


def testKMEANS():
    data = pd.read_table("datasets/mouse.txt", engine='python', sep = ',', header=None )
    data = pp.scale(data)
    # setting cols names
    # TODO: set standard names to N columns or use default pandas names assigns
    data.columns = ['x','y']
    # instanciating kmeans
    km = K_means(data, k=3, alpha=0.001)

    # updating algorithm
    km.update()

    # plotting the final result
    km.plot()

def testKNN():
    # objetivo: com base nos dados, predizer qual é a liga do jogador
    data = pd.read_table("datasets/Skillcraft/SkillCraft1_Dataset.csv", engine='python',na_values='?', sep = ',', header=0 )
    
    # pre processing

    # remove rows with anormal data
    k = data.loc[data['TotalHours']>100000].index[0] # 0 to select the index, not the data type (1)
    data = data.drop(k,axis=0) # removing data

    # separating data from answers
    answers = data['LeagueIndex']

    # removing useless data column: Age, LeagueIndex, GameID, HoursPerWeek, TotalHours
    data = data.drop(data.columns[:5], axis = 1) # parei aqui

    knn = KNN(data, answers)
        
    knn.createConfMatrix(248) # knn.saveMatrix() ?

    # # select random player
    # rindex = random.randint(0,len(data))
    # rp = data.loc[rindex]
    # data = data.drop(rindex, axis = 0) # remove random player from dataset
    # rpLeague = rp['LeagueIndex'] # extract random player league
    # rp = rp[5:] # remove useless data


    # print(knn.getKNN(rp))


# testKNN()
testKMEANS()