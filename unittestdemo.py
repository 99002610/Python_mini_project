import csv
your_list=[]
with open('DB.csv', newline='') as f:
    reader = csv.reader(f)
    your_list = list(reader)
