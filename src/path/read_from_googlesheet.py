#!/usr/bin/env python3

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import sys
from aggregate_data import AggregateData


class ReadFromGooglesheet():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Country name Project-0e6407319613.json', scope)
    client = gspread.authorize(creds)
    sh = client.open('Country name project').sheet1
    result = sh.col_values(6)
    outputfilename = '/home/fahim/Downloads/Country name project/temp/data_from_googlesheets.json'
    with open(outputfilename, 'wb') as outfile:
        json.dump(result, outfile)

    print('finish1')

    AggregateData()


ReadFromGooglesheet()
