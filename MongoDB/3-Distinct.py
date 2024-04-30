from pymongo import MongoClient

client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 1 - lista o mapeamento de generos
print(db.laureates.distinct('gender'))

# 2 - lista o mapeamento de categorias dos prêmios
print(db.laureates.distinct('prizes.category'))

# 3 - Quais categorias do prêmio, além de física, tem laureado com ações trimestrais?
print(db.laureates.distinct('prizes.category', {'prizes.share': "4"}))

# 4 - Quais categorias de laureados ganharam mais de um prêmio
print(db.laureates.distinct(
  'prizes.category',
  {'prizes.1': {'$exists': True}}
))