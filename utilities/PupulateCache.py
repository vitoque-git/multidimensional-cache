import random

# Define the number of records and maximum integer for key values
from constants import *
from utilities.Timer import Timer

# Generate random search parameters
def random_search_params():
    return {key: random.randint(1, max_int) for key in KEY_FIELDS}

# Create random data
def create_random_data(cache,num_records):
    _create_random_data(cache, num_records, max_int, key_distribution)

def _create_random_data(cache, num_records, max_int, key_distribution):
    """
    Populate a cache with random data.

    Parameters:
    cache (MultiDimensionalCacheBase): The cache instance to populate.
    num_records (int): The total number of records to add to the cache.
    max_int (int): The maximum integer value for the key values.
    key_distribution (dict): A dictionary defining the distribution of records
                             with a specific number of keys. Keys should be integers
                             from 1 to 5, and values should be floats representing
                             the proportion of records to generate for that key count.

    Example:
    key_distribution = {
        1: 0.1,  # 10% of records will have 1 key
        2: 0.2,  # 20% of records will have 2 keys
        3: 0.3,  # 30% of records will have 3 keys
        4: 0.2,  # 20% of records will have 4 keys
        5: 0.2   # 20% of records will have 5 keys
    }
    """

    # Example usage
    timer = Timer()
    timer.start()
    keys = KEY_FIELDS

    def random_params(num_keys):
        return {k: random.randint(1, max_int) for k in random.sample(keys, num_keys)}

    records_per_key_count = {k: int(v * num_records) for k, v in key_distribution.items()}

    i = 0
    for num_keys, count in records_per_key_count.items():
        for _ in range(count):
            params = random_params(num_keys)
            value = f"Value_{num_keys}_{i}"
            cache.add_to_cache(params, value)
            i = i + 1

    timer.end(True,"Data populated")

