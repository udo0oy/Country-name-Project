#!/usr/bin/env python3


import json
import sys  
from phonetics import metaphone
from cluster_data import ClusterData


class AggregateData():
    json_data = json.load(open('/home/fahim/Downloads/Country name project/temp/data_from_googlesheets.json'))
    
    
    
    
    print(json_data)
    ClusterData()
    print('finish2')

AggregateData()
