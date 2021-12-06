# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:29:21 2020

@author: Peter
"""

import pandas as pd
import cleaner_module as cm
import persist_models
import ARIMA_model as am


title = 'Weekly Installs Forecast'
project_data = 'PATH_TO_DATA'
project_path = 'PATH_TO_PROJECT'
frequency = 'W-Mon' #week starting on Monday
seasonality = 5 #found from tests/charts
forecast_period = 12

##clean data by referencing other script and create df
df = cm.get_cleaned_data(project_data)

#transform df into timeseries
timeseries = pd.Series(df.iloc[:,1].values,
                        index = pd.date_range(df.iloc[0]['Date'], periods = len(df.index), freq=frequency))


##check if model already exists/persists
try:
    arima_model = persist_models.load_model(project_path,title)
    MODEL_EXISTS = True
    print('model already exists')
except:
    MODEL_EXISTS = False
    print('existing model not found...')
    

if MODEL_EXISTS == False:
    """Make a new model if no model exists so far"""
    print('making new model...')
    #make stationarity and seasonlity tests
    import ts_modelling_tests as mt
    mt.stationarity_test(timeseries)
    mt.stl_decompose(timeseries, seasonality)
    mt.correlation_plots(timeseries)
    
    ##create ARIMA model and predictions
    arima_model = am.create_arima_model(timeseries, seasonality)
    
   
#create a forecast from the model with plots etc.
forecast_df = create_forecasts_from_arima_model(timeseries, arima_model, forecast_period, title)


##Persisting model if we made a new one
if MODEL_EXISTS == False:
    print('persisting new model...')
    persist_models.persist_model(project_path, title, arima_model)
    


