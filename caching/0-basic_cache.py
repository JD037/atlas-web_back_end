#!/usr/bin/env python3
"""
0-basic_cache.py - BasicCache class implementation
Create a class BasicCache that inherits from BaseCaching
and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesnt have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesnt exist in self.cache_data, return None
"""

from base_caching import BaseCaching


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
