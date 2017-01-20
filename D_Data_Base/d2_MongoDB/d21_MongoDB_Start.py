import pymongo

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

for item in sheet_tab.find({'words':{'$lt':5}}):
    print(item)
