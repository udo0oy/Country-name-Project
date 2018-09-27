#!/usr/bin/env python3

import sys
from read_from_googlesheet import GooglesheetReader
from aggregate_data import DataAggregator
from cluster_data import DataCluster
from distance_calculate import DistanceCalculator
from write_to_googlesheet import GooglesheetWritter

def main():
    reader = GooglesheetReader()
    reader.read()
    
    DataAggregator()
    DataCluster()
    DistanceCalculator()
    GooglesheetWritter()

if __name__ == '__main__':
    main()
