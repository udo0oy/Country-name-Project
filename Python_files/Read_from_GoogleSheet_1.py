#!/usr/bin/env python3

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import sys  
sys.path.insert(0, r'/home/fahim/Downloads/Country name project/Python_files') 
from Aggregate_data_2 import Aggregate_data

class Read_from_GoogleSheet():
    
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Country name Project-0e6407319613.json',scope)
    client = gspread.authorize(creds)
    sh =  client.open('Country name project').sheet1
    #pp = pprint.PrettyPrinter()
    result = sh.col_values(1)
    #pp.pprint(result)
    outputfilename="/home/fahim/Downloads/Country name project/JSON_Files/data_from_GoogleSheets_1.json"
    with open(outputfilename, 'wb') as outfile:
        json.dump(result, outfile)
    Aggregate_data()
    print('finish1')
if __name__ == '__main__':
    Read_from_GoogleSheet()

