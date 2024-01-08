#!/usr/bin/env python3
"""
Module 4-mru_cache.py with MRUCache class implementation.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements MRU caching.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.key_access_order = []

    def put(self, key, item):
        """
        Add an item to the cache using MRU strategy.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_access_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recently_used_key = self.key_access_order.pop(-1)
                del self.cache_data[most_recently_used_key]
                print("DISCARD:", most_recently_used_key)
            self.key_access_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key and update its position in the access order.
        """
        if key is not None and key in self.cache_data:
            self.key_access_order.remove(key)
            self.key_access_order.append(key)
            return self.cache_data[key]
        return None
