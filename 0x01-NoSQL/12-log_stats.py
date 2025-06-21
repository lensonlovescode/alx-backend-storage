#!/usr/bin/env python3
"""
Contains a script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == '__main__':
    """
    Summarizes nginx logs stored in the database
    """
    client = MongoClient()
    collection = client.logs.nginx

    listOfMethods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    logs = collection.count_documents({})
    print(f"{logs} logs")

    print("Methods:")
    for method in listOfMethods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
