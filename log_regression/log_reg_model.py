# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:54:32 2020

@author: Peter
"""

# =============================================================================
# Get Data. Will be sent from retention_forecast_main.py
# =============================================================================
def make_log_reg_model(df):
    
    import numpy as np
    from sklearn.model_selection import train_test_split
 
    train_df = df
    train_df.info()

    #make float values and split Y and X
    X = train_df.iloc[:,1:].values.astype('float')
    y = train_df['retention_state'].ravel() ##creates a flat, one-dimensional array

    ##split test and train
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)
    
    #check averages
    print('mean retention train: {0:.3f}'.format(np.mean(y_train)))
    print('mean retention test: {0:.3f}'.format(np.mean(y_test)))

    # =============================================================================
    # Performance Metrics
    # =============================================================================
    #inner function to print out performance metrics
    def get_performance_metrics(predictions, model_name):
        from sklearn.metrics import accuracy_score, confusion_matrix,precision_score,recall_score
        #accuracy score
        acc_score = accuracy_score(y_test,predictions)
        print_performance_message('Accuracy', model_name, acc_score)
        
        conf_matrix = confusion_matrix(y_test,predictions)
        print_performance_message('Confusion matrix', model_name, conf_matrix)
        
        precision = precision_score(y_test, predictions)
        print_performance_message('Precision', model_name, precision)
        
        recall = recall_score(y_test, predictions)
        print_performance_message('Recall', model_name, recall)
        
    #helper method for printing performance metrics
    def print_performance_message(metric_name, model_name, score):
        if metric_name == 'Confusion matrix':
            message = metric_name + ' for ' + model_name + ': \n {0}'.format(score)
        else:
            message = metric_name + ' for ' + model_name + ': {0:.3f}'.format(score)
        print(message)
    
    # =============================================================================
    # Baseline Model
    # =============================================================================
    from sklearn.dummy import DummyClassifier
    #create model
    model_dummy = DummyClassifier(strategy='most_frequent', random_state = 0)
    #train/fit model
    model_dummy.fit(X_train, y_train)
    #get metrics
    dummy_predictions = model_dummy.predict(X_test)
    get_performance_metrics(dummy_predictions, 'baseline_model')
    
    
    # =============================================================================
    # Logistic Regression
    # =============================================================================
    from sklearn.linear_model import LogisticRegression
    #create model
    model_logr_1 = LogisticRegression(C = 1.0, random_state = 0, solver = 'liblinear')
    #train/fit model
    results = model_logr_1.fit(X_train, y_train)
    
    #get predictictions
    predictions = model_logr_1.predict(X_test)
    
    #alternative prediction, if we want to put acceptance criteria to another value than 0.5
    #predictions = np.where(model_logr_1.predict_proba(X_test)[:,1] >= 0.4,1,0)
    
    print(predictions)
    
    #get metrics
    get_performance_metrics(predictions, 'model_logr_1')
    
    print('Intercepts:')
    print(model_logr_1.intercept_)

    print('Coefficients:')
    print(model_logr_1.coef_)
    
    print(results)
    
# =============================================================================
#         # p-values
# =============================================================================

    # from sklearn.feature_selection import chi2
    # scores, pvalues =chi2(X_train, y_train)
    # print('pvalues: ')
    # print(["{0:.7f}".format(x) for x in pvalues])
    
    # print(X_train)







