#!/usr/bin/env python3
import json
import sys


class DistanceCalculator():
    _User_Data = []
    _Name = []
    _Name_Count = []
    _Name_Metaphone = []
    _Output_File_Name = '../../temp/distance_calculated_data.json'
    _connection_file = '../../temp/clustered_data.json'
    _levenshtein_Value=int
    def read(self):
        connection_file = open(self._connection_file, 'r')
        try:
            qByUser = connection_file.read()
            self._User_Data = json.loads(qByUser)
        except ValueError:
            print
            'Decoding JSON has failed'
        connection_file.close()
        Distance_Calculator.divide()
    def divide(self):
        _list = list(self._User_Data.values())

        for  index,val in enumerate(self._User_Data):
            self._Name.append(val)
            self._Name_Count.append(_list[index][0]) 
            self._Name_Metaphone.append(_list[index][1]) 
        print(self._Name)
        print(self._Name_Count)
        print(self._Name_Metaphone)
        
        with open(self._Output_File_Name, 'w') as outfile:
            json.dump(self._User_Data, outfile,indent = 4)
        Distance_Calculator.compare()
    def compare(self):
        for  index_1,value_1 in enumerate(self._Name_Metaphone):
            for  index_2,value_2 in enumerate(self._Name_Metaphone):
               
                self._levenshtein_Value = Distance_Calculator.levenshtein(value_1,value_2)
                if (self._levenshtein_Value<=1):
                    print(str(self._Name[index_1])+" "+str(self._Name[index_2])+" "+ str(self._levenshtein_Value)+" "+str(value_1) + " " + str(value_2))
                    
    def levenshtein(self,s,t):
            if s == t: return 0
            elif len(s) == 0: return len(t)
            elif len(t) == 0: return len(s)
            v0 = [None] * (len(t) + 1)
            v1 = [None] * (len(t) + 1)
            for i in range(len(v0)):
                v0[i] = i
            for i in range(len(s)):
                v1[0] = i + 1
                for j in range(len(t)):
                    cost = 0 if s[i] == t[j] else 1
                    v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
                for j in range(len(v0)):
                    v0[j] = v1[j]
            x = v1[len(t)]
            return x

    
if __name__ == '__main__':
    Distance_Calculator = DistanceCalculator()
    Distance_Calculator.read()
