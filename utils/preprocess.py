import numpy as np

def preprocess_data(metrics):
    return np.array(metrics).reshape(1, -1)