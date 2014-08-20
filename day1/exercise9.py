from collections import defaultdict
import  matplotlib.pyplot as plt
import csv, sys, datetime
import pandas as pd
import re

#reader = csv.reader(open(sys.argv[1], 'r'))
newreattr = pd.DataFrame()
reader = pd.read_csv(sys.argv[1], skip_footer=1)

colNames = []
global bool
bool = False

global count
count = 0

for i in reader.columns:
    colNames.append(i)
print colNames


def stringSearchColumn_DataFrame(df, colName, regex):
     newreader = pd.DataFrame()
     newreader = newreader.fillna(0)
 
     for idx, record in reader[colName].iteritems():
         global bool
         bool = False

         global count
         count = 0

         if re.search(regex, str(record)):
              bool = True
              newreader = pd.concat([reader[reader[colName] == record], newreader], ignore_index=True)
              
              if bool:
                   print "Field that contains REATTRIBUTION text:" + colName
                   
              count+=1
              if count == 1:
                   break
                   
     return newreader
     

for idx, val in enumerate(colNames):
    #print val
    stringSearchColumn_DataFrame(reader, val, "REATTRIBUTION")
    
