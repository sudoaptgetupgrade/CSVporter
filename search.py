# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
database = client["bangolufsen"]
collection = database["masterdealerlist"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

chosecity = input("What city?: ")

query = {}
query["$or"] = [
    {
        u"City": 'chosecity'
    }
]


projection = {}
projection["Name"] = 1.0
projection["Street"] = 1.0
projection["Postal Code"] = 1.0
projection["City"] = 1.0
projection["_id"] = 0.0

sort = [ (u"Name", 1) ]

cursor = collection.find(query, projection = projection, sort = sort)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()
