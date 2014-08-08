import csv,sys,datetime
reader = csv.DictReader(open(sys.argv[1], 'r'))
for row in reader:
    name = row['cand_nm']
    datestr = row['contb_receipt_dt']
    amount = float(row['contb_receipt_amt'])
    if amount < 0:
        line = '\t'.join(row.values())
        print line
