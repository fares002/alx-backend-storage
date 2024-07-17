#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Return a list of all documents in a collection or an empty list
    """
    colls = mongo_collection.find()
    return [coll for coll in colls]
