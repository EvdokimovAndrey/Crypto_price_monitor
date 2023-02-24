import numpy as np
import pandas as pd
from sklearn import linear_model


class Prediction:

    def get_predict_eth(y):

      btc = pd.read_csv(r"HistoricalData_1677240295811.csv", encoding="windows-1251", sep=",")
      eth = pd.read_csv(r"HistoricalData_1677240284174.csv", encoding="windows-1251", sep=",")


      btc['Close/Last-eth'] = eth['Close/Last']

      btc['Date'] = pd.to_datetime(btc['Date'])

      train = btc[btc.Date<'01/01/2022']
      test = btc[btc.Date>='01/01/2022']

      X_train = np.array(train['Close/Last'])
      y_train = np.array(train['Close/Last-eth'])

      X_test = np.array(test['Close/Last'])
      y_test = np.array(test['Close/Last-eth'])


      lm = linear_model.LinearRegression()
      lm.fit(X_train.reshape(-1,1), y_train)

      y_pred = lm.predict(X_test.reshape(-1,1))

      y_pred = lm.predict(np.array([y]).reshape(-1,1))

      return y_pred