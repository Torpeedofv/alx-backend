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

        length = len(self.cache_data)
        if key not in self.cache_data and\
                len(self.cache_data) >= self.MAX_ITEMS:
            lfu = min(self.frequency.values())
            lfu_keys = []
            for k, v in self.frequency.items():
                if v == lfu:
                    lfu_keys.append(k)
            if len(lfu_keys) > 1:
                lru_lfu = {}
                for k in lfu_keys:
                    lru_lfu[k] = self.history.index(k)

                discard = min(lru_lfu.values())
                discard = self.history[discard]
            else:
                discard = lfu_keys[0]
            print("DISCARD:", discard)
            del self.cache_data[discard]
            del self.history[self.history.index(discard)]
            del self.frequency[discard]
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1
        if key in self.history:
            del self.history[self.history.index(key)]
        self.history.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """returns the item of a key"""
        if key is not None and key in self.cache_data.keys():
            del self.history[self.history.index(key)]
            self.history.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
