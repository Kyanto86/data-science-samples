# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:22:47 2020

@author: Peter
"""

def persist_model(project_path, title, model):
    import pickle
    import os
    
    model_title = title + '.pkl'
    
    model_file_path = os.path.join(project_path,'Models', model_title)
    
    #open files to write
    model_file_pickle = open(model_file_path, 'wb')
    #persist the model
    pickle.dump(model, model_file_pickle)
    #close the files.
    model_file_pickle.close()
    
    print('model persisted!')
    
    
def load_model(project_path, title):
    import pickle
    import os
    
    model_title = title + '.pkl'
    model_file_path = os.path.join(project_path,'Models', model_title)
    
    #open files in read mode
    model_file_pickle = open(model_file_path, 'rb')
    
    #load files
    model_loaded = pickle.load(model_file_pickle)
    
    #close files
    model_file_pickle.close()
    
    return model_loaded