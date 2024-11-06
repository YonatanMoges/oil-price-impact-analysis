# Brent Oil Price Analysis and Dashboard
This project analyzes Brent oil prices and builds an interactive dashboard to visualize historical trends, forecast prices, and study the correlation with global events and economic indicators. The analysis is implemented in Python, while the dashboard is built with Flask (backend) and React (frontend).

## Table of Contents
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Tasks](#tasks)
  - [Task 2: Data Collection and Analysis](#task-2-data-collection-and-analysis)
  - [Task 3: Dashboard Development](#task-3-dashboard-development)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
  - [Starting the Backend](#starting-the-backend)
  - [Starting the Frontend](#starting-the-frontend)
- [Technologies Used](#technologies-used)

## Project Structure
The project directory is organized as follows:

```plaintext
project-root/
├── data/                           # Contains raw and processed data files
│   ├── BrentOilPrices.csv
│   ├── Preprocessed_BrentOilPrices.csv
│   └── Economic_Data.csv
|
├── notebooks/
|   └──price_analysis.ipynb         # Demonstration of price analysis
├── scripts/                        # Python scripts for analysis
│   └── price_analysis.py
├── src/
│   ├── api/                        # Flask backend
│   │   ├── app.py                  # Main Flask application
│   │   ├── endpoints.py            # API endpoints
│   └── frontend/                   # React frontend
│       ├── public/
│       │   └── index.html          # Main HTML file for React app
│       └── src/
│           ├── App.js              # React main component
│           ├── index.js            # React entry point
│           ├── components/
│           │   └── Dashboard.js    # Dashboard component
├──requirements.txt                # Dependencies
└── README.md                       # Project documentation
```
## Setup
### Prerequisites
Python 3.8+  
Node.js 14+ and npm  
Flask for the backend and React for the frontend  
World Bank API Access for fetching economic data  

### Installation
Clone the repository

```bash
git clone <repository-url>
cd project-root
```

Setup Virtual Environment for Backend (Flask)
``` bash
python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
cd src/api
# Install dependencies
pip install -r requirements.txt
```

Install Frontend Dependencies (React)

```bash
cd ../frontend
npm install
```

## Tasks
### **Data Collection and Analysis**
This task involves gathering Brent oil prices and economic indicators from the World Bank API, preprocessing, and performing exploratory analysis and forecasting.

### **Steps:**
1. **Load Brent Oil Prices Data**
Load data from BrentOilPrices.csv (located in data/), which contains historical oil prices.

2. **Fetch Economic Data**
Use the fetch_economic_data method in price_analysis.py to collect indicators like GDP, inflation, unemployment, and exchange rate. Data is saved as Economic_Data.csv.

3. **Data Preprocessing Process**
Preprocess and merge Brent oil prices with economic data. Save the preprocessed data to Preprocessed_BrentOilPrices.csv.

4. **Model Training and Forecasting**
Train ARIMA and VAR models on the preprocessed data:
ARIMA for univariate oil price forecasting.  
VAR for multivariate forecasting incorporating economic indicators.  
Performance Evaluation Evaluate models using RMSE, MAE, and R² metrics.

#### **Features of Data Collection and Analysis**

The `scripts/price_analysis.py` file contains a PriceAnalysis class for preprocessing both oil data and economic data fetched from the World Bank's API. The `notebooks/price_analysis.ipynb` notebook provides an example of running preprocessing and performing model training and forecasting.

### **Dashboard Development**  
Build an interactive dashboard to visualize the analysis results, making insights accessible to stakeholders.

**Backend (Flask)
API Development**

`endpoints.py` provides routes to serve datasets and model results to the React frontend.  
Key endpoints:  
`/api/oil-data` — Returns oil price data.  
`/api/economic-data` — Returns economic indicators.  
`/api/forecast` — Provides forecasting results.  

**Run Flask Backend**

Navigate to the src/api directory and start the backend:
```bash
python app.py
```
**Frontend (React)
React Application Setup**

`Dashboard.js` in src/compnents fetches and displays data from the Flask API.  


**Run React Frontend**

Navigate to src/frontend and start the React app:
```bash
npm start
```
#### **Key Features of the Dashboard**
- Data Visualization: Historical trends, model forecasts, and economic indicators.
- Event Highlighting: Show spikes and drops related to specific events.
- Filters and Comparisons: Filter by date range and event type for custom views.
- Performance Metrics: Display RMSE, MAE, and R² values.
#### **API Endpoints**
- /api/oil-data: Returns Brent oil price data.
- /api/economic-data: Serves economic indicators.
- /api/forecast: Provides the forecast from ARIMA/VAR models.
- /api/metrics: Returns model performance metrics (RMSE, MAE, etc.).

## Usage
### **Starting the Backend**
Navigate to API directory:

```bash
cd src/api
```
Run Flask Server:

```bash
python app.py
```

### **Starting the Frontend**
Navigate to Frontend directory:

```bash
cd src/frontend
```
Run React Application:

``` bash
npm start
```
## Technologies Used
Python (Flask) — API development and model serving.  
JavaScript (React) — Interactive frontend for visualization.  
Pandas, Statsmodels — Data preprocessing and modeling.  
Recharts, Chart.js — Data visualization in React.  
World Bank API — Economic data collection.

