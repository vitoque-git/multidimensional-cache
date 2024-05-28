from utilities.PupulateCache import *
from utilities.Timer import Timer
import numpy as np


def do_test(cache, num_records=None, data=None, search_dataset=None):
    if data is None:
        # Create random data
        create_random_data(cache, num_records)
    else:
        cache.cache = data

    try:
        # only compiled cache has compile_patterns
        cache.compile_patterns()
    except:
        pass

    # Perform the cache search X times with randomized parameters
    num_iterations = 10000

    search_times = []
    attempt_iteractions = []
    timer = Timer()

    hits = 0

    if search_dataset is None:
        search_dataset = []
        for _ in range(num_iterations):
            # the search parameters are random in each attempt
            search_dataset.append(random_search_params())

    for search_params in search_dataset:
        # the search parameters are random in each attempt
        timer.start()

        #search this value
        value, number_attempts = cache.search_cache(search_params)

        #mantain stats
        elapsed_time = timer.end()
        if value is not None:
            hits = hits + 1
        search_times.append(elapsed_time)
        attempt_iteractions.append(number_attempts)


    # Print statistics
    print("----------------------------------------", num_records, type(cache))
    print(f"Hits : {hits} out of {num_iterations} ({hits/num_iterations:.1f}%)")
    print(f"Average search time: {np.mean(search_times):.6f} ms")
    print(f"99th percentile search time: {np.percentile(search_times, 99):.6f} ms")
    print(f"Minimum search time: {np.min(search_times):.6f} ms")
    print(f"Maximum search time: {np.max(search_times):.6f} ms")

    print(f"Average attempts: {np.mean(attempt_iteractions):.1f}")
    return np.mean(search_times), search_dataset


