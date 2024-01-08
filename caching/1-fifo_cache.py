#!/usr/bin/env python3
"""
Module 1-fifo_cache.py with FIFO class implementation
Create a class FIFOCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    and implements FIFO caching.
    """

    def __init__(self):
        """
        Initialize the class.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO strategy.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest_key = self.key_order.pop(0)
                    del self.cache_data[oldest_key]
                    print("DISCARD:", oldest_key)
                self.key_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
