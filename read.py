#reading csv file using dictreader class
import csv
reader= csv.DictReader(open("sec_bhavdata_full.csv"))
for raw in reader:
    print (raw)