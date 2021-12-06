# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:27:36 2020

@author: Peter
"""

import matplotlib.pyplot as plt

#Exponential Forecasting model
def create_EXPSmodel(timeseries, seasonality, forecast_periods, plot_title):

    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    
    expsmodel = ExponentialSmoothing(timeseries, trend = 'add', seasonal = 'additive', seasonal_periods= seasonality)
    expsmodelfit = expsmodel.fit()
    expsfcast = expsmodelfit.forecast(forecast_periods)
    
    plot_title = plot_title + " EXPS"
    
    plt.figure(figsize=(12,8))
    plt.plot(timeseries, label = 'actuals')
    plt.plot(expsfcast, label = 'forecast')
    plt.title(plot_title)
    plt.legend()
    
    

#FB Prophet Model
def create_prophet_model(timeseries, forecast_periods, frequency):
    
    import pandas as pd
    from fbprophet import Prophet
    
    prophet_df = pd.DataFrame({'ds':timeseries.index, 'y':timeseries.values})
    
    prophet_model = Prophet()
    prophet_model.fit(prophet_df)
    
    future_data = prophet_model.make_future_dataframe(periods = forecast_periods, freq = frequency)
    fcast = prophet_model.predict(future_data)
    
    fig, ax1 = plt.subplots(1,1,figsize=(12,8))
    prophet_model.plot(fcast, ax = ax1)
    plt.ylabel('Installs')
    plt.xlabel('Time')
