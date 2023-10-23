#!/usr/bin/python3
"""A module for a child class"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """creation of a lfu cache"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.history = []
        self.frequency = {}

    def put(self, key, item):
        """add a new key, item to the cache"""
        if key is None or item is None:
            return

        if key not in self.cache_data and\
                len(self.cache_data) >= self.MAX_ITEMS:

