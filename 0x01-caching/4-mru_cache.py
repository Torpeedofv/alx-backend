#!/usr/bin/python3
"""A module for a child class"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """creation of a mru cache class"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.history = []

    def put(self, key, item):
        """add a new key, item to the cache"""
        if key is None or item is None:
            return

        if key not in self.cache_data and\
                len(self.cache_data) >= self.MAX_ITEMS:
            print("DISCARD:", self.history[-1])
            self.cache_data.pop(self.history[-1])
            del self.history[-1]
        if key in self.history:
            del self.history[self.history.index(key)]
        self.history.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """returns the item of a key"""
        if key is None or key not in self.cache_data:
            return None
        del self.history[self.history.index(key)]
        self.history.append(key)
        return self.cache_data[key]
