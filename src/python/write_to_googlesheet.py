#!/usr/bin/env python3

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GooglesheetWritter():
    _User_Data = []
    _Name = []
    _Name_Count = []
    _Name_Metaphone = []
    _temp_val=[]
    _temp_key=[]
    _scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    _cred = '../conf/credential.json'
    _gsheet = 'Country name project'
    _inputfilename = '../../temp/distance_calculated_data.json'
    def read(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(self._cred, self._scope)
        client = gspread.authorize(creds)
        sh = client.open(self._gsheet).get_worksheet(1)
        cell_list0 = sh.range('A1:A1000')
        cell_list1 = sh.range('B1:B1000')	
        cell_list2 = sh.range('C1:C1000')
        
        connection_file = open(self._inputfilename, 'r')
        try:
            qByUser = connection_file.read()
            self._User_Data = json.loads(qByUser)
        except ValueError:
            print
            'Decoding JSON has failed'
        connection_file.close()
        _list = list(self._User_Data.values())
        for  index,val in enumerate(self._User_Data):
            self._Name.append(val)
            self._Name_Count.append(_list[index][0]) 
            self._Name_Metaphone.append(_list[index][1]) 
                   
        #print(self._User_Data)
        print (len(self._temp_key))
        for i, val in enumerate(self._Name):
            cell_list0[i].value = self._Name[i]
            cell_list1[i].value = self._Name_Count[i]
            cell_list2[i].value = self._Name_Metaphone[i]
        sh.update_cells(cell_list0)	
        sh.update_cells(cell_list1)	
        sh.update_cells(cell_list2)
if __name__ == '__main__':
    Googlesheet_Writter = GooglesheetWritter()
    Googlesheet_Writter.read()
