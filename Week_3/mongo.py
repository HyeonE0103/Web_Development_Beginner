from pymongo.mongo_client import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.local

collection = db.fastcampus

# collection.insert_one({
#     "title": "Fastcampus Course!",
#     "Content": "3 Week Course"
# })

collection.insert_one({
    "title": "Yeah",
    "Content": "Yeah~ Party Tonight!"
})

# row = collection.find_one()   find로 하면 결과값이 cursor로 뜸 
# print(row)                    cursor는 반복할 수 있는 데이터

rows = collection.find()        #반복문을 이용해 안에 데이터를 확인할 수 있음
for row in rows:
    print(row)

row = collection.find_one({'title': "Fastcampus Course!"})
print(row)