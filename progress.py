from datetime import date
from time import sleep
from tqdm import tqdm

today = date.today()
start_date = date(2019,1,28)
end_date = date(2023,1,28)
total = end_date - start_date
completed = today - start_date
progress = int(completed.days)

print("Enric Moreu's PhD progress:")
for i in tqdm(range(0,365*4), bar_format='{n}/{total} days ({percentage:2.0f}%) [{bar}]'):
    sleep(0.01)
    if i > progress: 
        break
