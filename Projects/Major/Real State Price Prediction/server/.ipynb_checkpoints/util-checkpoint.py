{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7d7e6418",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "loading saved artifacts...start\n",
      " loading artifacts is done\n",
      "53.29\n",
      "70.95\n",
      "89.78\n",
      "64.66\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\sklearn\\base.py:409: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\sklearn\\base.py:409: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\sklearn\\base.py:409: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n",
      "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\sklearn\\base.py:409: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "import joblib\n",
    "import numpy as np\n",
    "__locations = None\n",
    "__area = None\n",
    "__model = None\n",
    "\n",
    "\n",
    "def get_estimated_price(area_type, location, size, total_sqft, bath, balcony):\n",
    "    x = np.zeros(6)\n",
    "    x[0] = __area.index(area_type)\n",
    "    x[1] = __locations.index(location)\n",
    "    x[2] = size\n",
    "    x[3] = total_sqft\n",
    "    x[4] = bath\n",
    "    x[5] = balcony\n",
    "    \n",
    "    return round(__model.predict([x])[0][0],2)\n",
    "    \n",
    "\n",
    "def locations():\n",
    "    return __locations\n",
    "def areas():\n",
    "    return __area\n",
    "\n",
    "def load_saved_artifacts():\n",
    "    print(\"loading saved artifacts...start\")\n",
    "    global __data_columns\n",
    "    global __locations\n",
    "    global __area\n",
    "    \n",
    "    with open('./artifacts/locations.json','r') as f:\n",
    "        __locations = json.load(f)['data_locations']\n",
    "    \n",
    "    with open('./artifacts/area.json','r') as f:\n",
    "        __area = json.load(f)['data_area']\n",
    "       \n",
    "    global __model\n",
    "    \n",
    "    __model = joblib.load('./artifacts/Banglore_Real_State_Price')\n",
    "    print(\" loading artifacts is done\")\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    load_saved_artifacts()\n",
    "    #print(locations())\n",
    "    #print(areas())\n",
    "    \n",
    "    print(get_estimated_price('Super built-up  Area','Electronic City Phase II',2,1056,2,1))\n",
    "    print(get_estimated_price('Built-up  Area','Uttarahalli',3,1440,2,3))\n",
    "    print(get_estimated_price('Super built-up  Area','Lingadheeranahalli',3,1521,3,1))\n",
    "    print(get_estimated_price('Super built-up  Area','Kothanur',2,1200,2,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "462ad97b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
