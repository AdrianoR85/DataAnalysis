from pymongo import MongoClient

# 1 - Establish a connection with MongoDB and Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 2 - Count by the number of genres
print(db.laureates.count_documents({"gender": "female"}))
print(db.laureates.count_documents({"gender": "male"}))

# 3 - Count documents by country that died
print(db.laureates.count_documents({"diedCountry": "France"}))

# 4 - Filter 
filter_doc = {
  "diedCountry": "France",
  "gender": "female",
  "bornCity": "Warsaw"
}
print(db.laureates.count_documents(filter_doc))
# print(db.laureates.find_one(filter_doc))

# 5 - IN operator
filter_in = db.laureates.count_documents({
  "diedCountry": {
    "$in": ["France", "USA"]
  }
})
print(filter_in)

# 6 - NE
filter_ne = db.laureates.count_documents({
  "diedCountry": {
    "$ne": "USA"
  }
})
print(filter_ne)