from collections import defaultdict
from itertools import combinations

from caches.AshedCache import AshedCache
from constants import *
from utilities.Timer import Timer


class AshedCacheCompiled(AshedCache):
    def __init__(self):
        super().__init__()
        self.matching_pattern = defaultdict(dict)

    def generate_keys(self, params):
        """
        Generate all possible keys with decreasing number of parameters.
        """
        keys = []
        param_keys = list(params.keys())
        for i in range(len(param_keys), 0, -1):
            for combo in combinations(param_keys, i):
                if self.matching_pattern[combo]:
                    key = tuple((k, params[k]) for k in combo)
                    keys.append(key)
        return keys

    def has_matching_data(self, key_combination):
        """
        Check if the cache contains any data that matches the given key combination.

        Parameters:
        cache (HierarchicalMultiDimensionalCache): The cache instance to search.
        key_combination (tuple): The combination of keys to search for.

        Returns:
        bool: True if the cache contains data matching the key combination, False otherwise.
        """
        for key in self.cache.keys():
            if sorted([k[0] for k in key]) == sorted(key_combination):
                # print(key)
                return True
        return False

    def compile_patterns(self):
        timer = Timer()
        timer.start()
        self._compile_patterns(KEY_FIELDS)
        timer.end(True, "Created valid matching pattern")
        count = 0
        for value in self.matching_pattern.values():
            if value:
                count += 1
        print('Valid patterns', count, 'of', len(self.matching_pattern))

    def _compile_patterns(self, param_keys):
        """
        Check all possible combinations of the provided parameter keys to see if they
        match any rule in the cache. Cache the results.

        Parameters:
        param_keys (list): A list of parameter keys to check.
        """
        # Iterate over all lengths of combinations from the length of param_keys down to 1
        for i in range(len(param_keys), 0, -1):
            # Generate all combinations of param_keys of length i
            for combo in combinations(param_keys, i):
                # Check if the current combination matches any data in the cache
                has_matching_pattern = self.has_matching_data(combo)
                # Cache the result of whether this combination has matching data
                self.matching_pattern[combo] = has_matching_pattern



