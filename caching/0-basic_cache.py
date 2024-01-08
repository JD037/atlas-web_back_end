#!/usr/bin.env python3
"""
0-basic_cache.py - BasicCache class implementation
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache system class
    """


def put(self, key, item):
    """
    Assign the item value for the key in self.cache_data
    """
    if key is not None and item is not None:
        self.cache_data[key] = item


def get(self, key):
    """
    Return the value in self.cache_data linked to the key
    """
    if key is None or key not in self.cache_data:
        return None
    return self.cache_data.get(key)
