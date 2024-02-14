# 8-all.py
def list_all(mongo_collection):
    return list(mongo_collection.find())
