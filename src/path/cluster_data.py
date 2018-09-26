#!/usr/bin/env python3

import json
from phonetics import metaphone

class DataCluster():
    User_Data= []
    Metaphone_User_Data = []

    connection_file = open('/home/fahim/Downloads/Country name project/temp/aggregated_data.json', 'r')
    try:
        qByUser = connection_file.read()
        User_Data = dict(json.loads(qByUser))
    except ValueError:
        print
        'Decoding JSON has failed'
    connection_file.close()

    for index, val in enumerate(User_Data):
        print(str(index + 1) + ". " + val + " = " + metaphone(val))
        Metaphone_User_Data.append(metaphone(val))

    To_Add=dict(zip(User_Data,Metaphone_User_Data))

    for key, val in To_Add.items():
        if key in User_Data:
            User_Data[key] = [User_Data[key], val]

    outputfilename = '/home/fahim/Downloads/Country name project/temp/clustered_data.json'
    with open(outputfilename, 'w') as outfile:
        json.dump(User_Data, outfile)

    print(User_Data)

        #Code will be needed future
'''for index,valu in enumerate(User_Data)
    def appender(data, metaphones):
        return data.append[metaphones]
    Clustered_User_Data= dict(map(appender,User_Data,Metaphone_User_Data))
    #print(str(len(Metaphone_User_Data)))

    for index_1, value_1 in enumerate(Metaphone_User_Data):
        for index_2, value_2 in enumerate(Metaphone_User_Data):
            print( value_1 +"("+str(index_1)+") == "+value_2 +"("+str(index_2)+")")
            if value_1 == value_2:
                Clustered_User_Data.append(User_Data[index_2])
                print("Deleting "+ User_Data[index_2])
                del User_Data[index_2]
                print(str(len(Clustered_User_Data)) + "  " + Clustered_User_Data[-1] +" "+ str(len(User_Data)))
                print("Deleting " + Metaphone_User_Data[index_2])
                del Metaphone_User_Data[index_2]

    for v,val in enumerate(Clustered_User_Data):
        print(str(v) + " " + val);'''
print('finish3')

DataCluster()
