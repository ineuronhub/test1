import pymongo
client = pymongo.MongoClient("mongodb+srv://mongo:database@cluster0.ktfqv3a.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name" : "jagruti",
    "surnamw" : "wagh",
    "email" : "jagrutiwagh2320@gmail.com"
}
d={
    "name" : "suyash",
    "surnamw" : "wagh",
    "email" : "jagrutiwagh2320@gmail.com"
}
d={
    "name" : "Dipak",
    "surnamw" : "wagh",
    "email" : "jagrutiwagh2320@gmail.com"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )