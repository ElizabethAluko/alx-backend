#!/usr/bin/env python3
"""Base Dictionary Module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Basic dictionary Caching"""
    def __init__(self):
        """Initialize the class with the super class init method"""
        super().__init__()
        self.key_frequency = {}
        self.current_time = 0

    def update_frequency(self, key):
        if key in self.key_frequency:
            self.key_frequency[key] += 1
        else:
            self.key_frequency[key] = 1

    def put(self, key, item):
        """Set the nee value"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= super().MAX_ITEMS:
            items = [k for k, v in self.key_frequency.items()
                     if v == min(self.key_frequency.values())]
            if len(items) > 1:
                item = min(items, key=lambda k: self.key_frequency[k])
                items.remove(item)
                item_to_discard = min(items, key=lambda k: self.key_frequency[k])
            else:
                item_to_discard = items[0]
            print('DISCARD: {}'.format(item_to_discard))
            self.cache_data.pop(item_to_discard)
            self.key_frequency.pop(item_to_discard)

        # Insert new item
        self.cache_data[key] = item
        self.update_frequency(key)
        self.current_time += 1

    def get(self, key):
        """Retrieve the value of the given key"""
        if key in self.cache_data:
            self.update_frequency(key)
            self.current_time += 1
            return self.cache_data[key]

        else:
            return None
