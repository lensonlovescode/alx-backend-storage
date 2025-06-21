#!/usr/bin/env python3
"""
Contains a function that lists all documents in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    mongolia = []
    for collection in mongo_collection.find():
        mongolia.append(collection)

    return mongolia
