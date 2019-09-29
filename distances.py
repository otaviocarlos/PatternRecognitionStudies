import random
import numpy as np
import scipy

class Dist():
    @staticmethod
    def euclid(p1,p2):
        if len(p1) != len(p2):
            raise Exception("tuples must be the same size")

        s = 0
        for i in range(len(p1)):
            s += (p1[i]-p2[i])**2

        return np.sqrt( s )

    @staticmethod
    def manhattan(p1,p2):
        if len(p1) != len(p2):
            raise Exception("tuples must be the same size")

        s = 0
        for i in range(len(p1)):
            s += np.abs(p1[i]-p2[i])

        return s
    @staticmethod
    def correlation(p1,p2, absVal = True):
        if len(p1) != len(p2):
            raise Exception("tuples must be the same size")

        n = len(p1)
        s1 = np.std(p1)
        s2 = np.std(p2)
        m1 = np.mean(p1)
        m2 = np.mean(p2)

        cima = n*np.sum(p1*p2) - np.sum(p1)*np.sum(p2)
        baixo = np.sqrt(n*np.sum(p1**2) - np.sum(p1)**2 )*np.sqrt(n*np.sum(p2**2) - np.sum(p2)**2 )

        res = (1 - ( cima / baixo )) if absVal else ( cima / baixo )

        return res



# PLOT = False
# points = np.array([[2,1,2,2,5],[4,3,4,2,5]])

# print("\nmanhattan: ",  manhattan(points[0],points[1]))
# print("euclidian: ",    euclid(points[0],points[1]))
# print("abscorrelation: ",  correlation(points[0],points[1]))
# print("correlation: ",  correlation(points[0],points[1], absVal=False))