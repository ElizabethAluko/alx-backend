#!/usr/bin/python3
"""Base Dictionary Module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary Caching"""
    MAX_ITEMS = 10 ** 1000

    def __init__(self):
        """Initialize the class with the super class init method"""
        super().__init__()

    def put(self, key, item):
        """Set the nee value"""
        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value of the given key"""
        if key in self.cache_data:
            return(self.cache_data[key])
        else:
            return None

