# src/api/endpoints.py
from flask import Blueprint, jsonify
import pandas as pd

data_blueprint = Blueprint("data", __name__)

oil_data = pd.read_csv('../../data/Preprocessed_BrentOilPrices.csv')
economic_data = pd.read_csv('../../data/Economic_Data.csv')
combined_data = pd.read_csv('../../data/Combined_Data.csv')

# Define endpoints
@data_blueprint.route('/api/oil_data', methods=['GET'])
def get_oil_data():
    return oil_data.to_json(orient='records')

@data_blueprint.route('/api/economic_data', methods=['GET'])
def get_economic_data():
    return economic_data.to_json(orient='records')

@data_blueprint.route('/api/combined_data', methods=['GET'])
def get_combined_data():
    return combined_data.to_json(orient='records')

# Additional routes for model metrics, specific events, etc.
