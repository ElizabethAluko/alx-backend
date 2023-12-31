#!/usr/bin/env python3
"""Base Dictionary Module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Basic dictionary Caching"""
    def __init__(self):
        """Initialize the class with the super class init method"""
        super().__init__()

    def put(self, key, item):
        """Set the nee value"""
        if key is None or item is None:
            return

        elif key in self.cache_data:
            del self.cache_data[key]

        elif len(self.cache_data) >= super().MAX_ITEMS:
            first_key, _ = next(iter(self.cache_data.items()))
            del self.cache_data[first_key]
            print('DISCARD: {}'.format(first_key))
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value of the given key"""
        if key in self.cache_data:
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return (self.cache_data[key])

        else:
            return None
