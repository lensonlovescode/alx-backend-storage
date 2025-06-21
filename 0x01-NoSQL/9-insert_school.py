#!/usr/bin/env python3
"""
Contains a funtion that inserts a document to collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a doc into a collection based on kwargs
    """
    return mongo_collection.insert(kwargs)
