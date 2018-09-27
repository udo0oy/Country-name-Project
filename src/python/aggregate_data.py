#!/usr/bin/env python3

import json

class DataAggregator():
    User_Data = []
    connection_file = open('/home/fahim/Downloads/Country name project/temp/data_from_googlesheets.json', 'r')
    try:
        qByUser = connection_file.read()
        User_Data = json.loads(qByUser)
    except ValueError:
        print
        'Decoding JSON has failed'
    connection_file.close()


    def get_cnt(lVals):
        d = dict(zip(lVals, [0] * len(lVals)))
        for x in lVals:
            d[x] += 1
        return d

    sortDic = dict(sorted(get_cnt(User_Data).items()))

    outputfilename = '/home/fahim/Downloads/Country name project/temp/aggregated_data.json'
    with open(outputfilename, 'w') as outfile:
        json.dump(sortDic, outfile)
    print(sortDic)
    print('finish2')


DataAggregator()
