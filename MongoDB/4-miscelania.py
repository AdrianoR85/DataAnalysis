from pymongo import MongoClient

client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 1 - Todos Laureados que possuem prêmios em física e compartilhados.
print(db.laureates.count_documents({
  'prizes': {
    '$elemMatch':{
      'category': 'physics',
      'share': '1'
    }
  }
}))

# 1 - Todos Laureados que possuem prêmios em física e compartilhados antes de 1945.
print(db.laureates.count_documents({
  'prizes': {
    '$elemMatch':{
      'year': {'$lt': '1945'}, #lt = menor que, gt = maior que
      'category': 'physics',
      'share': '1'
    }
  }
}))

# 4  - Regex - Alguns Laureados  nasceram em lugares que se tornariam a Polônia
print(db.laureates.distinct(
  'bornCountry',
  {'bornCountry': {'$regex': 'Poland'}}
))

