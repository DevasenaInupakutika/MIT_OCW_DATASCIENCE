from collections import defaultdict
import  matplotlib.pyplot as plt
import csv, sys, datetime

reader = csv.DictReader(open(sys.argv[1], 'r'))

obamadonations = defaultdict(lambda:0)
mccaindonations = defaultdict(lambda:0)

for row in reader:
    name = row['cand_nm']
    datestr = row['contb_receipt_dt']
    amount = float(row['contb_receipt_amt'])
    date = datetime.datetime.strptime(datestr, '%d-%b-%y')


    if 'Obama' in name:
        obamadonations[date] += amount
    if 'McCain' in name:
        mccaindonations[date] += amount

# dictionaries
sorted_by_date1 = sorted(obamadonations.items(), key=lambda (key,val): key)
xs,ys = zip(*sorted_by_date1)

sorted_by_date2 = sorted(mccaindonations.items(), key=lambda (key,val): key)
xt,yt = zip(*sorted_by_date2)

lines = plt.plot(xs, ys, xt, yt)

plt.legend(loc='upper center', ncol = 4)

plt.savefig('Plotobcain.png', format='png')
