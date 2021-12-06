# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:54:55 2020

@author: Peter
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:57:16 2020

@author: Peter
"""


import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
#SAMPLE_SPREADSHEET_ID = 'SHEET_ID'
#SAMPLE_RANGE_NAME = 'RANGE_NAME'

def main(pd_dataframe, SHEET_ID, RANGE_NAME, method):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    print("entered gsheets")
    
    global values, service
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r'PATH_TO_CREDENTIALS', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    writeToSheet(pd_dataframe, SHEET_ID, RANGE_NAME, method)
    

def writeToSheet(pd_dataframe,SHEET_ID,RANGE_NAME, method):
    
    print("entered writeToSheet")
    
   
    #if we append we don't need headers, and we want to call the append function
    if method == "APPEND":
        
        body = dict(majorDimension = 'ROWS',
        values = pd_dataframe.values.tolist())
        
        result = service.spreadsheets().values().append(
            spreadsheetId=SHEET_ID, range=RANGE_NAME,
       valueInputOption='RAW', body=body
            ).execute()
        
        print("Sheet appended.")

    #we overwrite (i.e. don't append, which means we need the column names too.)    
    else:
        
        body = dict(majorDimension = 'ROWS',
        values = [pd_dataframe.columns.values.tolist()] + pd_dataframe.values.tolist())
    
        result = service.spreadsheets().values().update(
            spreadsheetId=SHEET_ID, range=RANGE_NAME,
        valueInputOption='RAW', body=body
            ).execute()
    
        print("Sheet updated.")

