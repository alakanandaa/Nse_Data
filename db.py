#importing necessary packages
import pandas as pd
from pymongo import MongoClient
client=MongoClient()
db=client.PracticeNSE # storing data to db created
data=db.nse
df=pd.read_csv("sec_bhavdata_full.csv")
records=df.to_dict(orient= 'records') #storing data in record format
result=db.nse.insert_many(records)


