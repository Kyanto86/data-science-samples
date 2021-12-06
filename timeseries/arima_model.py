# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:13:09 2020

@author: Peter
"""

####ARIMA MODEL#####

def create_arima_model(timeseries, period):
    
    import pmdarima as pm
    
    ##if -1 then we don't look for seasonality.
    if period == -1:
        arima_model = pm.auto_arima(timeseries, seasonal = False,
                     stepwise = False, trace = True, error_action='ignore', suppress_warnings=True)

    ##else period is the number of days we look for seasonality
    else:
        arima_model = pm.auto_arima(timeseries, seasonal = True, m = period,
                     stepwise = False, trace = True, error_action='ignore', suppress_warnings=True)
    arima_model.summary()
    arima_model.plot_diagnostics(figsize =(8,8))
    
    print('order: ' + str(arima_model.order))
    print('seasonal_order: ' + str(arima_model.seasonal_order))
    print('AIC: ' + str(arima_model.aic()))
    return arima_model

