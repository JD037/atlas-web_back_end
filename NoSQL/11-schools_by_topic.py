# 11-schools_by_topic.py
def schools_by_topic(mongo_collection, topic):
    return list(mongo_collection.find({"topics": topic}))
