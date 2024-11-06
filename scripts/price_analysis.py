import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import wbdata
import datetime
import warnings
warnings.filterwarnings('ignore')

class PriceAnalysis:
    def __init__(self, oil_data, economic_data=None, countries=['USA']):
        self.oil_data = oil_data
        self.economic_data = economic_data
        self.countries = countries
        self.model_results = {}
    
    def preprocess_data(self):
        # Convert dates to datetime format
        self.oil_data['Date'] = pd.to_datetime(self.oil_data['Date'])
        self.oil_data.set_index('Date', inplace=True)
        self.oil_data['Price'] = pd.to_numeric(self.oil_data['Price'], errors='coerce')
        self.oil_data = self.oil_data.dropna()
        
        if self.economic_data is not None:
            self.economic_data['Date'] = pd.to_datetime(self.economic_data['Date'])
            self.economic_data.set_index('Date', inplace=True)
            self.data = self.oil_data.join(self.economic_data, how='inner')
        else:
            self.data = self.oil_data
    
    def fetch_economic_data(self, start_year=2010, end_year=2022):
        indicators = {
            "NY.GDP.MKTP.KD.ZG": "GDP Growth (annual %)",
            "FP.CPI.TOTL.ZG": "Inflation, consumer prices (annual %)"
        }
        start_date = datetime.datetime(start_year, 1, 1)
        end_date = datetime.datetime(end_year, 1, 1)
        
        # Fetch data
        data_frames = []
        for country in self.countries:
            country_data = wbdata.get_dataframe(indicators, country=country, data_date=(start_date, end_date), convert_date=True)
            data_frames.append(country_data)
        
        # Merge data if multiple countries selected
        self.economic_data = pd.concat(data_frames, axis=1)
        print("Economic data fetched successfully.")
        
    def exploratory_data_analysis(self):
        # Plot oil prices
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Price'], color='blue')
        plt.title('Brent Oil Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price (USD per barrel)')
        plt.show()
        
        # Correlation heatmap
        if self.economic_data is not None:
            plt.figure(figsize=(8, 6))
            sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm')
            plt.title('Correlation Matrix')
            plt.show()
    
    def train_arima_model(self, order=(1, 1, 1)):
        model = ARIMA(self.oil_data['Price'], order=order)
        arima_result = model.fit()
        self.model_results['ARIMA'] = arima_result
        print(arima_result.summary())
    
    def train_var_model(self, lag_order=1):
        if self.economic_data is not None:
            model = VAR(self.data)
            var_result = model.fit(lag_order)
            self.model_results['VAR'] = var_result
            print(var_result.summary())
        else:
            print("VAR model requires economic data.")
    
    def forecast_arima(self, steps=30):
        if 'ARIMA' in self.model_results:
            forecast = self.model_results['ARIMA'].forecast(steps=steps)
            return forecast
        else:
            print("Train ARIMA model before forecasting.")
    
    def evaluate_model(self, true_values, predicted_values):
        mse = mean_squared_error(true_values, predicted_values)
        mae = mean_absolute_error(true_values, predicted_values)
        r2 = r2_score(true_values, predicted_values)
        print(f'MSE: {mse}, MAE: {mae}, R2: {r2}')
    
    def train_and_evaluate_all_models(self):
        # Train ARIMA
        self.train_arima_model()
        arima_forecast = self.forecast_arima()
        
        # Evaluate ARIMA model
        if arima_forecast is not None:
            self.evaluate_model(self.oil_data['Price'][-30:], arima_forecast)

        # Train VAR model if economic data is available
        if self.economic_data is not None:
            self.train_var_model()
        else:
            print("Economic data not available, skipping VAR model.")
