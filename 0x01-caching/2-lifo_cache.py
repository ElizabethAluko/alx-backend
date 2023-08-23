#!/usr/bin/env python3
"""Base Dictionary Module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Basic dictionary Caching"""

    def __init__(self):
        """Initialize the class with the super class init method"""
        super().__init__()

    def put(self, key, item):
        """Set the nee value"""
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            if len(self.cache_data) >= super().MAX_ITEMS:
                last_key, last_item = self.cache_data.popitem()
                print('DISCARD: {}'.format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value of the given key"""
        if key in self.cache_data:
            return (self.cache_data[key])
        else:
            return None
