#!/usr/bin/env python3
""" FIFO caching """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """  that inherits from BaseCaching """

    def __init__(self):
        """  """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ dictionary from the parent class """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """ Must return the value in self """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
