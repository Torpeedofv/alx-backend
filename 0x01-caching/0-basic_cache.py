#!/usr/bin/python3
"""A module that contains a class that inherits from a base class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Creation of a child class"""
    def put(self, key, item):
        """adds a new key and item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets an item using the key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
