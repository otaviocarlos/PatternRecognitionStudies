from sklearn import preprocessing
import pandas as pd
import numpy as np

class PreProcessing():
    @staticmethod
    def scale(data):
        data = data.astype(float)
        scaler = preprocessing.MinMaxScaler()
        data = scaler.fit_transform(data)

        return pd.DataFrame(data)