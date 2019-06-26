import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client.NSEDB
collection_1=db.all_data
collection_2=db.Company_Symbol
data=collection_1.find({})
data_list = list(data)
i = 0
for x in data_list:
     data_dict = data_list[i]
     print( data_dict["SYMBOL"] +" , " +data_dict[' SERIES']) # extracting Symbol and series field of all documents from Mongodb and printing
     i = i+1
