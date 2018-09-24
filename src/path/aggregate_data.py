#!/usr/bin/env python3

import json
import sys  
from phonetics import metaphone

class DataAggregator():
    qUserData=[]
    connection_file = open('/home/fahim/Downloads/Country name project/temp/data_from_googlesheets.json', 'r')
    try:
        qByUser = connection_file.read()
        qUserData = json.loads(qByUser)
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print
        'Decoding JSON has failed'
    connection_file.close()
    print('finish2')

DataAggregator()