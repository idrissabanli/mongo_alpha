import pymongo

myclient = pymongo.MongoClient("mongodb://root:12345@localhost:27017/")

mydb = myclient['logger']

mycol = mydb['main.py']
for x in mycol.find({'is_worked': False}):
    print(x['args'])
