import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

class TransactionForecasting:
    def __init__(self, data):
        self.data = data

    def prepare_data(self):
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data.set_index('date', inplace=True)

    def fit_arima_model(self, p, d, q):
        self.model = ARIMA(self.data, order=(p, d, q))
        self.model_fit = self.model.fit()

    def forecast_transactions(self, steps):
        forecast = self.model_fit.forecast(steps=steps)
        return forecast

    def evaluate_model(self, forecast, actual):
        mse = mean_squared_error(actual, forecast)
        return mse

# Example usage:
data = pd.read_csv('transaction_data.csv')
transaction_forecasting = TransactionForecasting(data)
transaction_forecasting.prepare_data()
transaction_forecasting.fit_arima_model(p=1, d=1, q=1)
forecast = transaction_forecasting.forecast_transactions(steps=30)
print(forecast)
