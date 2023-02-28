!pip install yfinance
import yfinance as yf
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import sklearn.model_selection as model_selection 
import math
import keras.losses as keras_losses

# get data from yfinance
btc = yf.Ticker("BTC-USD")
df = btc.history(period="max",start="2023-01-01",end="2023-02-28")

# set data
data = df[['Close']]
data = data.set_index(pd.DatetimeIndex(df.index))

# normalize data
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# create lstm model
X = data_scaled[0:len(data_scaled)-1]
y = data_scaled[1:]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=0)
X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
X_test = X_test.reshape(X_test.shape[0], 1, X_test.shape[1])

# create lstm model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# fit model
model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=1)

# make forecasts
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# invert predictions
train_predict = scaler.inverse_transform(train_predict)
y_train = scaler.inverse_transform(y_train)
test_predict = scaler.inverse_transform(test_predict)
y_test = scaler.inverse_transform(y_test)

# calculate root mean squared error
train_score = math.sqrt(keras_losses.mean_absolute_error(y_train[0], train_predict[:,0]))
print('Train Score: %.2f RMSE' % (train_score))
test_score = math.sqrt(keras_losses.mean_squared_error(y_test[0], test_predict[:,0]))
print('Test Score: %.2f RMSE' % (test_score))

# shift train predictions for plotting
train_predict_plot = np.empty_like(data_scaled)
train_predict_plot[:, :] = np.nan
train_predict_plot[1:len(train_predict)+1, :] = train_predict

# shift test predictions for plotting
test_predict_plot = np.empty_like(data_scaled)
test_predict_plot[:, :] = np.nan
#test_predict_plot[len(train_predict)+(1*2)+1:len(data_scaled)-1, :] = test_predict

# plot baseline and predictions
plt.plot(scaler.inverse_transform(data_scaled))
plt.plot(train_predict_plot)
plt.plot(test_predict_plot)
plt.show()


# Predict the price 24 hours later
prediction_date = pd.date_range('2023-02-28', periods=2, freq='D')[1]
prediction_date_df = pd.DataFrame([[prediction_date]], columns = ['Date'])
prediction_X = scaler.transform(prediction_date_df)
prediction_X = prediction_X.reshape(1, 1, 1)
prediction_price = model.predict(prediction_X)
prediction_price = scaler.inverse_transform(prediction_price)

print("Predicted price 24 hours later: ", prediction_price[0][0])
