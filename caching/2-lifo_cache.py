#!/usr/bin/env python3
"""
module 2-lifo_cache.py with LIFOCache class implementation.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements LIFO Caching.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Add an item to the cache using LIFO strategy.
        """
        if key is not None and item is not None:
            if (key not in self.cache_data and
                    len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                last_key = self.key_order.pop(-1)
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            elif key in self.cache_data:
                self.key_order.remove(key)
            self.key_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item by key.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
