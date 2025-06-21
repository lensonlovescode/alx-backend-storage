#!/usr/bin/env python3
"""
Contains a function that changes all topics of a school document based on name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school doc based on name
    """
    tps = {"topics": topics}
    return (mongo_collection.update_many({"name": name}, {"$set": tps}))
