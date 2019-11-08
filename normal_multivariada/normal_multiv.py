import numpy as np

class Func:
    def __init__(self, mu, covm):
        self.mu = mu
        self.covm = covm


def multivarNormal(x, f):
    k = x.ndim
    p1 = (2*np.pi)**(-k/2)

    # p2 = determinant da matriz de cov elevado à -1/2
    det = np.linalg.det(f.covm)
    p2 = det**(-1/2)

    # p3 = exp da forma quadrática
    dif = (x - f.mu)
    difT = dif.transpose()
    inv = np.linalg.inv(f.covm)
    p3 = np.exp( (-1/2)*(dif.dot(inv).dot(difT)) ) 
    
    return p1*p2*p3


# entra ponto no eixo XY, retorna o valor no eixo Z
f1 = Func(np.array([0,0]),np.array([[1,3/5],[3/5,1]]))
res = multivarNormal(np.array([2,-2]), f1)
print(res)

