import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD

X = np.array([[0,0],[0,1],[1,0],[1,1]]) # XOR inputs
y = np.array([[0],[1],[1],[0]]) # XOR outputs

model = Sequential()

model.add(Dense(8, input_dim=2)) # input of 2 dimensions, hidden layer with 8 nodes
model.add(Activation('relu'))
model.add(Dense(1)) # boolean output
model.add(Activation('sigmoid'))

model.compile(loss='mean_squared_error', optimizer = 'adam', metrics = ['binary_accuracy']) # SGD(lr=0.1) stocastic gradient descendent

model.fit(X, y, nb_epoch=3000, verbose = 2)

print(model.predict_proba(X))

'''
[[0.00212344]
 [0.9949292 ]
 [0.9952442 ]
 [0.00621163]]
'''