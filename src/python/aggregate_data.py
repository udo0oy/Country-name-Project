#!/usr/bin/env python3

import json

class DataAggregator(object):
    _User_Data = []
    _connection_file = '../../temp/data_from_googlesheets.json'
    _outputfilename = '../../temp/aggregated_data.json'


    def read(self):
        connection_file=open(self._connection_file, 'r')
        try:
            qByUser = connection_file.read()
            self._User_Data = json.loads(qByUser)
        except ValueError:
            print
            'Decoding JSON has failed'
        connection_file.close()

        sortDic = dict(sorted(get_cnt(self._User_Data).items()))

        with open(self._outputfilename, 'w') as outfile:
            json.dump(sortDic, outfile)

def get_cnt(lVals):
    d = dict(zip(lVals, [0] * len(lVals)))
    for x in lVals:
        d[x] += 1
    return d

if __name__ == '__main__':
    Data_Aggregator = DataAggregator()
    Data_Aggregator.read()
