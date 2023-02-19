import json
import pickle
import sklearn
import numpy as np
import warnings

warnings.filterwarnings('ignore')

__locations = None
__area = None
__model = None

def get_estimated_price(area_type, location, size, total_sqft, bath, balcony):
    x = np.zeros(6)
    x[0] = __area.index(area_type)
    x[1] = __locations.index(location)
    x[2] = size
    x[3] = total_sqft
    x[4] = bath
    x[5] = balcony

    return round(__model.predict([x])[0][0], 2)

def locations():
    global __locations

    with open('./artifacts/locations.json', 'r') as f:
        __locations = json.load(f)['data_locations']
    return __locations
def areas():
    global __area

    with open('./artifacts/area.json', 'r') as f:
        __area = json.load(f)['data_area']

    return __area

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __locations
    global __area

    with open('./artifacts/locations.json', 'r') as f:
        __locations = json.load(f)['data_locations']

    with open('./artifacts/area.json', 'r') as f:
        __area = json.load(f)['data_area']

    global __model
    with open('./artifacts/Banglore_Real_State_Price.pickle', 'rb') as f:
        __model = pickle.load(f)

    print(" loading artifacts is done")


if __name__ == '__main__':
    load_saved_artifacts()
    if None not in __locations:
        print ("ok")
    #print(locations())
    #print(areas())

    print(get_estimated_price('Super built-up  Area','Electronic City Phase II',2,1056,2,1))
    print(get_estimated_price('Built-up  Area','Uttarahalli',3,1440,2,3))
    print(get_estimated_price('Super built-up  Area','Lingadheeranahalli',3,1521,3,1))
    print(get_estimated_price('Super built-up  Area','Kothanur',2,1200,2,1))

