from utilities.PupulateCache import create_random_data, random_search_params
from caches.AshedCache import AshedCache
from utilities.Timer import Timer
import numpy as np

cache = AshedCache()

# Create random data
create_random_data(cache)

# Example search
# Perform the cache search 1000 times with randomized parameters
num_iterations = 200
search_times = []
attempt_iteractions = []
timer = Timer()

for _ in range(num_iterations):
    search_params = random_search_params()
    timer.start()
    value, number_attempts = cache.search_cache(search_params)
    elapsed_time = timer.end()
    search_times.append(elapsed_time)
    attempt_iteractions.append(number_attempts)

# Print statistics
print(f"Average search time: {np.mean(search_times):.6f} ms")
print(f"99th percentile search time: {np.percentile(search_times, 99):.6f} ms")
print(f"Minimum search time: {np.min(search_times):.6f} ms")
print(f"Maximum search time: {np.max(search_times):.6f} ms")

print(f"Average attempts: {np.mean(attempt_iteractions):.1f}")