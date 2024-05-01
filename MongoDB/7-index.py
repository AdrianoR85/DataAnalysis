from pymongo import MongoClient

client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']


def get_all_prizes_economics():
  list(db.prizes.find(
    {'category': 'economics'},
    {'year':1, '_id':0}
  ))

