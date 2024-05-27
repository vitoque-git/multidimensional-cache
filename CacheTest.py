from caches.AshedCacheCompiled import AshedCacheCompiled
from constants import NUM_RECORDS
from utilities.PupulateCache import create_random_data, random_search_params
from caches.AshedCache import AshedCache
from utilities.Timer import Timer
import numpy as np

cache = AshedCacheCompiled()
# cache = AshedCache()

# Create random data
create_random_data(cache, num_records=NUM_RECORDS)

try:
    cache.compile_patterns()
except:
    pass

# Example search
# Perform the cache search 1000 times with randomized parameters
num_iterations = 10000

search_times = []
attempt_iteractions = []
timer = Timer()

hits = 0


for _ in range(num_iterations):
    # the search parameters are random in each attempt
    search_params = random_search_params()
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
print("----------------------------------------")
print(f"Hits : {hits} out of {num_iterations} ({hits/num_iterations:.1f}%)")
print(f"Average search time: {np.mean(search_times):.6f} ms")
print(f"99th percentile search time: {np.percentile(search_times, 99):.6f} ms")
print(f"Minimum search time: {np.min(search_times):.6f} ms")
print(f"Maximum search time: {np.max(search_times):.6f} ms")

print(f"Average attempts: {np.mean(attempt_iteractions):.1f}")