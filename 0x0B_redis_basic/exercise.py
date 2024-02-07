#!/usr/bin/env python3
"""
Module for basic operations with Redis.
"""

import redis
import uuid
from typing import Union, Callable

class Cache:
    """
    Cache class for storing data in Redis.
    """
    def __init__(self):
        """
        Initialize the Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key.
        
        Args:
        data: The data to be stored, which can be a str, bytes, int, or float.
        
        Returns:
        A string representing the randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
