import numpy as np
from catboost import CatBoostRegressor
import pickle

pickle_in = open('cb_model.pkl', 'rb') 
cb_model = pickle.load(pickle_in)



def get_prediction(data,model):
    """
    Predict the class of a given data point.
    """
    return model.predict(data)
