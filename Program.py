#!/usr/bin/env python3

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
# ''' From Wikipedia article; Iterative with two matrix rows. '''
def levenshtein(s, t):
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
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Country name Project-0e6407319613.json',scope)
client = gspread.authorize(creds)
sh =  client.open('Country name project').sheet1
pp = pprint.PrettyPrinter()
result = sh.col_values(6)
##pp.pprint(result)


cell_list1 = sh.range('B1:B500')
cell_list2 = sh.range('C1:C500')
for i, val in enumerate(result): 
 cell_list1[i].value=val

sh.update_cells(cell_list1)               # Update in batch
count=0                                   # For counting same input
cellcount= 0                              # For counting which cell to use
for i, val in enumerate(result,0): 
 for j, valu in enumerate(result,0): 
  if val!=None and valu != None:   
   x=levenshtein(val,valu)
   if x == 0 :
    count=count+1
    print('levenshtein ' + val + ' and ' +valu+ ' is :  '+str(x) )  
   if count > 0:
    cell_list1[j].value = None
    cell_list2[j].value = None
 cell_list1[cellcount].value = val
 cell_list2[cellcount].value = count   
 count=0
 cellcount = cellcount + 1

for i, val in enumerate(cell_list1,0):
   if cell_list1[i].value != None:
     for j, val in enumerate(cell_list1,0):
         if cell_list1[j].value == None:
             cell_list1[j].value = cell_list1[i].value
             cell_list2[j].value = cell_list2[i].value
             cell_list1[i].value = None
             cell_list2[i].value = None

#pp.pprint(cell_list1)
#pp.pprint(cell_list2)
sh.update_cells(cell_list1) # Update in batch
sh.update_cells(cell_list2) # Update in batch
tempname = sh.range('D1:D500')
tempcount= sh.range('E1:E500')
cell1 = sh.col_values(2)
cell2 = sh.col_values(3)
cell_list1=cell1
cell_list2=cell2
count = 0
for i, val in enumerate(cell_list1,0):
 if val != None:
  print("1st value "+val)   
  for j ,valu in enumerate(cell_list1,0):
   if valu !=None :
    x=levenshtein(val,valu)
    print(val+" with "+valu + " is "+ str(x)) 
    if x < 4:
     tempname[i].value=val
     tempcount[i].value=valu
     if x !=0:
      val=None
      valu=None
      count=count+1
 if x==0:
  val=None
  valu=None
for i, val in enumerate(tempname,1):
 print(tempname[i].value)
 cell_list1[i].value=val
for i, val in enumerate(tempcount,1): 
 cell_list2[i].value=val 
sh.update_cells(tempname) # Update in batch
sh.update_cells(tempcount) # Update in batch

