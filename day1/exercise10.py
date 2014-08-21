from collections import defaultdict
import  matplotlib.pyplot as plt
import csv, sys, datetime
import pandas as pd
import re

#reader = csv.reader(open(sys.argv[1], 'r'))
newreattr = pd.DataFrame()
reader = pd.read_csv(sys.argv[1], skip_footer=1)
reader1 = csv.DictReader(open(sys.argv[1], 'r'))

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

     global obamadonations
     global mccaindonations

     global ob
     global mc

     obamadonations = defaultdict(lambda:0)
     mccaindonations = defaultdict(lambda:0)

     ob = 0.0
     mc = 0.0
 
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
                   for row in reader1:
                       name = row['cand_nm']
                       datestr = row['contb_receipt_dt']
                       amount = float(row['contb_receipt_amt'])
                       date = datetime.datetime.strptime(datestr, '%d-%b-%y')
		       desc = row['receipt_desc']
                       memo = row['memo_text']

    
                       if 'Obama' in name: 
                            if 'REATTRIBUTION TO SPOUSE' in row[colName]:
                                 obamadonations[date]+=amount
 				 ob = obamadonations[date]
   
    
                       if 'McCain' in name:
                            if 'REATTRIBUTION TO SPOUSE' in row[colName]:
                                 mccaindonations[date]+=amount
                                 mc = mccaindonations[date]

                   print "Obama Donations for RATS:", ob
                   print "Mc Cain donations for RATS:" , mc
              
                   count+=1

              if count == 1:
                   break
                   
     
     return newreader
     

for idx, val in enumerate(colNames):
    #print val
    stringSearchColumn_DataFrame(reader, val, "REATTRIBUTION")
    
