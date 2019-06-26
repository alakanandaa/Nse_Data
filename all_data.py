#inserting  multiple csv files to mongodb
import csv
import pymongo
from pymongo import MongoClient
import pandas as pd
import glob

client = MongoClient()
db = client.NSEDB
data = db.all_data
extension = "csv"
files = [i for i in glob.glob('*.{}'.format(extension))]
df=pd.concat([pd.read_csv(f) for f in files])
records = df.to_dict(orient='records')
result = db.all_data.insert_many(records)
