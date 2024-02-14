#!/usr/bin/env python3
"""11-schools_by_topic.py"""

def schools_by_topic(mongo_collection, topic):
    """Function that returns a list of school having a specifi topic"""
    return list(mongo_collection.find({"topics": topic}))
