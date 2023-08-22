#!/usr/bin/env python3
"""Base Dictionary Module for basic Caching illustration"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary Caching with BaseCaching as base"""

    def __init__(self):
        """Initialize the class with the super class init method"""
        super().__init__()

    def put(self, key, item):
        """Set the new value of key to item"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value of the given key"""
        if key in self.cache_data:
            return (self.cache_data[key])
        else:
            return None
