#!pip install yfinance
import json
import datetime
import yfinance as yf

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.preprocessing import MinMaxScaler

def GetData(usd, dt, fromDay, toDay):
  fromDate = dt - datetime.timedelta(days=fromDay)
  toDate = dt - datetime.timedelta(days=toDay)
  df = yf.download(usd, fromDate, toDate, interval = "1d")[['Close']]#, 'Open', 'Low', 'High', 'Volume']]
  return df.to_json()

usd = 'BTC-USD'
loop = 2000

startTime = datetime.datetime.now()
total = GetData(usd, startTime, 365, 0)

dataset_train = pd.read_json(GetData(usd, startTime, 365, 20))
training_set = dataset_train.iloc[:, 0:1].values

sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

X_train = []
y_train = []
for i in range(60, len(dataset_train)-(20)):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

regressor = Sequential()

regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units = 1))

regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

regressor.fit(x=X_train, y=y_train, epochs = loop, batch_size = 256, use_multiprocessing=True, workers=50)

dataset_test = pd.read_json(GetData(usd, startTime, 20, 0))
real_stock_price = dataset_test.iloc[:, 0:1].values
dataset_total = pd.concat((dataset_train[['Close']], dataset_test[['Close']]), axis = 0)

inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(60, len(inputs)):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
print(predicted_stock_price)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

plt.figure(figsize=(10,5))
plt.plot(real_stock_price, color = 'black', label = usd+' Price')
plt.plot(predicted_stock_price, color = 'green', label = 'Predicted '+usd+' Price')
plt.title(usd+' Prediction')
plt.xlabel('Day')
plt.ylabel(usd+' Price')
plt.xticks(np.arange(0, 20, 1.0))
plt.legend()
plt.show()

print('============START===========')
print(startTime)
print('============================')

print('============================')
print(datetime.datetime.now())
print('============END=============')
