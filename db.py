
import pandas as pd
from pymongo import MongoClient
client=MongoClient()
db=client.PracticeNSE
data=db.nse
df=pd.read_csv("sec_bhavdata_full.csv")
records=df.to_dict(orient= 'records')
result=db.nse.insert_many(records)


