from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.q15z7ue.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# movie = db.movies.find_one({'title':'가버나움'})
#
# star = movie['star']
#
# all_moives = list(db.movies.find({'star': star}, {'_id': False}))
#
# for m in all_moives:
#     print(m['title'])

db.movies.update_one({'title': '가버나움'}, {'$set': {'star': '0'}})