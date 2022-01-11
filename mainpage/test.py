from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mymongodb

doc = {'name':'testname', 'age':21}
db.users.insert_one(doc)