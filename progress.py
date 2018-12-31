from time import sleep
import sys
from datetime import date

today = date.today()
start_date = date(2018,12,1)
end_date = date(2023,2,1)
total = end_date - start_date
completed = today - start_date
progress = float(completed.days)/float(total.days)

print('PhD progress:')
for i in range(1+int(100 * progress)):
    print("\r[%-100s] %d%%" % ('='*i, i), end='\r')
    sleep(0.05)

