#!/usr/bin/python3
"""A module for a child class"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """creation of the child class"""
    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """add a new key, item to the cache"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                first_out = list(self.cache_data.keys())[0]
                del self.cache_data[first_out]
                print("DISCARD:", first_out)

    def get(self, key):
        """returns the item of a key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
