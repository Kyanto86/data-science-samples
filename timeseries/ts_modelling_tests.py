# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:44:21 2020

@author: Peter
"""

def stationarity_test (timeseries):
    """Augmented Dickey-Fuller test: A test for stationarity"""
    from statsmodels.tsa.stattools import adfuller
    import pandas as pd
    print("Result of ADF Test:")
    df_test = adfuller(timeseries, autolag = 'AIC')
    df_output = pd.Series(df_test[0:4], index = ['Test statistic', 'p-value', 'Number of lags used', 'Number of observations used'])
    print(df_output)
    

def stl_decompose (timeseries, period):
    from stldecompose import decompose
    import matplotlib.pyplot as plt
    
    if period == -1:
        stl_series = decompose(timeseries)
    else:
        stl_series = decompose(timeseries, period = period)
    
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize =(14,9))
    timeseries.plot(ax = ax1)
    stl_series.trend.plot(ax = ax2)
    stl_series.seasonal.plot(ax = ax3)
    stl_series.resid.plot(ax = ax4)
    ax1.set_title('Original')
    ax2.set_title('Trend')
    ax3.set_title('Seasonality')
    ax4.set_title('Residuals')
    plt.tight_layout()
    
    
def correlation_plots (timeseries):
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize=(12,8))
    ax1 = fig.add_subplot(211)
    fig = plot_acf(timeseries, lags = 20, ax = ax1)
    ax2 = fig.add_subplot(212)
    fig = plot_pacf(timeseries, lags = 20, ax = ax2)