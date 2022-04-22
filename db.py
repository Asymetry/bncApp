import pymongo

client = pymongo.MongoClient("mongodb+srv://hikmetozcnn:..hey29192121896@cluster0.ezcvw.mongodb.net/binanceFlask?retryWrites=true&w=majority")

mydb = client["binanceFlask"]
mycol = mydb["veriler"]


def add(data):
    x = mycol.insert_one(data)

    print(x.inserted_id)


def allData():
    data = []
    for i in mycol.find():
        data.append(i)

    return data

def delete(query):
    mycol.delete_one(query)

