import numpy as np

def stepFunction(soma):
    if (soma>=1):
        return 1
    return 0

def sigmoidFunction(soma):
    return 1/(1+np.exp(-soma))

def tahnFunction(soma): #tg hiperbolic function
    return (np.exp(soma) - np.exp(-soma))/(np.exp(soma)+np.exp(-soma))

def reluFunction(soma):
    if soma>= 0:
        return soma
    return 0

def linearFunction(soma):
    return soma

def softmaxFunction(x):
    #x is a vector
    ex = np.exp(x)
    return ex / ex.sum()