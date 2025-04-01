import json
import pickle
import numpy as np

__data_columns__ = None
__locations__ = None
__model__ = None
__type__ = None

def predict_price(location, type, beds, baths, sq_feet, furnishingb, smokingb, catsb, dogsb):
    global __data_columns__
    global __model__
    try:
        location_index = __data_columns__.index(location.lower())
        type_index = __data_columns__.index(type.lower())
    except:
        location_index = -1
        type_index = -1
    x = np.zeros(len(__data_columns__))
    x[0] = beds
    x[1] = baths
    x[2] = sq_feet
    x[3] = furnishingb
    x[4] = smokingb
    x[5] = catsb
    x[6] = dogsb
    x[location_index] = 1
    x[type_index] = 1

    return round(__model__.predict([x])[0], 2)

def get_location_names():
    load_saved_artifacts()
    return __locations__

def load_saved_artifacts():
    global __data_columns__
    global __locations__
    global __type__
    global __model__

    with open("./artifacts/columns.json", "r") as f:
        __data_columns__ = json.load(f)["data_columns"]
        __locations__ = __data_columns__[7:]
        __type__ = __data_columns__[-7:]

    with open("./artifacts/Canada_Rent_Prediction_Model.pickle", "rb") as f:
        __model__ = pickle.load(f)
    print("Done loading saved artifacts")

