import numpy as np

class ConfusionMatrix():
    def __init__(self, dim):
        self.dim = dim
        self.matrix = np.zeros([dim,dim])

    def validate(self, predict, real):
        # first value:
        best = predict.to_numpy()[0]
        # mean:
        # soma = 0
        # for i in range(len(results)):
        #     soma+=results[i]
        # predict = round(soma/len(results))

        # predict = int(stats.mode(results)[0][0]) # mode

        self.matrix[int(real-1)][best-1] += 1

    def showMatrix(self):
        print(self.matrix)

    def totalError(self, iterations):
        s = 0
        for i in range(self.dim):
            s += self.matrix[i][i]

        return 1-(s / iterations)