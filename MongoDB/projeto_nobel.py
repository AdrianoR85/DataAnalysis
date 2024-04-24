import requests
from pymongo import MongoClient

# 1 - Establish a connection with MongoDB and Database
client = MongoClient()
db = client['nobel']

# 2 - Import data in documents
for collection_name in ["prizes", "laureates"]:
  response = requests.get(
    f"https://api.nobelprize.org/v1/{collection_name[:-1]}.json")
  
  documents = response.json()[collection_name]
  db[collection_name].insert_many(documents)
  
prizes = db['prizes']
laureates = db['laureates']

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})
print(len_prizes)
print(len_laureates)