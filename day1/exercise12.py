from collections import defaultdict
import  matplotlib.pyplot as plt
import csv, sys, datetime
import pandas as pd
import re

newreattr = pd.DataFrame()
reader = pd.read_csv(sys.argv[1], skip_footer=1)
reader1 = csv.DictReader(open(sys.argv[1], 'r'))

global colNames
colNames = []

global bool
bool = False

global count
count = 0

for i in reader.columns:
    colNames.append(i)
print colNames

print colNames[2]

def stringSearchColumn_DataFrame(df, colName, regex):
     newreader = pd.DataFrame()
     newreader = newreader.fillna(0)

     reattr = pd.DataFrame()
     reattr = reattr.fillna(0)

     global obamadonations
     global mccaindonations

     obamadonations = defaultdict(lambda:0)
     mccaindonations = defaultdict(lambda:0)

 
     for idx, record in reader[colName].iteritems():
         global bool
         bool = False

         global count
         count = 0
 
	 global ob
         ob = 0.0

         global mc
         mc = 0.0

         if re.search(regex, str(record)):
              bool = True
              newreader = pd.concat([reader[reader[colName] == record], newreader], ignore_index=True)
              
              if bool:
                   print "Field that contains REATTRIBUTION text:" + colName
                   reattr = reader[reader[colName] == 'REATTRIBUTION TO SPOUSE']
                  
                   print "Column name for Candidates: ", colNames[2]
                   print "Column name for Donations amount: ", colNames[9]
                   print "Donation amounts column data: ", reader[colNames[9]]

                   for row in reader1:
                       if re.search('Obama', row[colNames[2]]):
                            ob+= float(row[colNames[9]])

                       if re.search('McCain', row[colNames[2]]):
	                    print row[colNames[9]]
                            mc+= float(row[colNames[9]])

                   print "Obama Donations: ", ob
                   print "Mc Cain Donations: ",mc

                   count+=1
                   
              
              if count == 1:
                   break
     return newreader
     

for idx, val in enumerate(colNames):
    #print val
    stringSearchColumn_DataFrame(reader, val, "REATTRIBUTION")
    
