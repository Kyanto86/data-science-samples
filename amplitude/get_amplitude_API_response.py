# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:50:41 2021

@author: Peter
"""

import requests
from requests.auth import HTTPBasicAuth

def get_api_response (chart_id):

    API_KEY = 'API_KEY'
    SECRET_KEY = 'SECRET_KEY'
    CHART_ID = chart_id
    ENDPOINT = 'https://amplitude.com/api/3/chart/' + CHART_ID + '/query'
    
    #connect to API and get response
    auth = HTTPBasicAuth(API_KEY,SECRET_KEY)
    response = requests.get(ENDPOINT, auth=auth)
    print('response code: ' + str(response.status_code) + '...chart: ' + chart_id)
    json_response = response.json()
    
    return json_response
