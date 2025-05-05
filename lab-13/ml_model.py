import pandas as pd 
import numpy as np 

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from math import radians, sin, cos, sqrt, atan2

data = pd.read_csv(r"C:\Users\lenovo\Desktop\Project 3\fare data.csv")
data = data.dropna()

data = data[(data['fare_amount'] > 0) & (data['fare_amount'] < 100)]
data = data[(data['passenger_count'] > 0) & (data['passenger_count'] <= 6)]

def haversine(lat1, lon1, lat2, lon2):
    R = 6371 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

data['distance'] = data.apply(lambda row: haversine(
    row['pickup_latitude'], row['pickup_longitude'],
    row['dropoff_latitude'], row['dropoff_longitude']), axis=1)

data = data[(data['distance'] > 0.5) & (data['distance'] < 50)]


X = data[['distance']]
y = data['fare_amount']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)


model = LinearRegression()
model.fit(X_train, y_train)

def predict_fare(distance):
    return model.predict([[distance]])[0]

if __name__ == "__main__":
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f'Mean Squared Error: {mse:.2f}')

    sample = 5 
    print(f'\nTesting | Distance: {sample} km -> Fare: ${predict_fare(sample):.2f} |')
