from pymongo import MongoClient

# 1 - Establish a connection with MongoDB and Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# Counting how many prizes by university
# laureates -> prizes -> affiliations -> name = search
california = db.laureates.count_documents({
  'prizes.affiliations.name': 'University of California'
})
print(california)

# Counting how many prizes by city
san_francisco = db.laureates.count_documents({
  'prizes.affiliations.city': 'San Francisco, CA'
})
print(san_francisco)

# Counting how many prizes exist
qtd_prizes = db.laureates.count_documents({
  'prizes': {
    '$exists': True
  }
})
print(qtd_prizes)

# Check if the prize is fill up
prizes_contain = db.laureates.count_documents({
  'prizes.0': {
    '$exists': True
  }
})
print(prizes_contain)

# Check if there is more than one prize
mult_prizes = db.laureates.count_documents({
  'prizes.1': {
    '$exists': True
  }
})
print(mult_prizes)