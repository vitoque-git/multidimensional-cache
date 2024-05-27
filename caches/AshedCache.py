from collections import defaultdict
from itertools import combinations

from caches.MultiDimensionalCacheBase import MultiDimensionalCacheBase


class AshedCache(MultiDimensionalCacheBase):
    def __init__(self):
        self.cache = defaultdict(dict)

    def add_to_cache(self, params, value):
        """
        Add a value to the cache with the given parameters.
        """
        key = tuple((k, params[k]) for k in params)
        self.cache[key] = value
        # print("Added", key, value)

    def generate_keys(self, params):
        """
        Generate all possible keys with decreasing number of parameters.
        """
        keys = []
        param_keys = list(params.keys())
        for i in range(len(param_keys), 0, -1):
            for combo in combinations(param_keys, i):
                key = tuple((k, params[k]) for k in combo)
                print(params,combo, keys)
                keys.append(key)
        return keys



    def search_cache(self, params):
        """
        Search the cache hierarchically with the given parameters.
        """
        keys = self.generate_keys(params)

        attempt_number = 0
        for key in keys:
            attempt_number = attempt_number + 1
            if key in self.cache:
                return self.cache[key], attempt_number
        return None, attempt_number
