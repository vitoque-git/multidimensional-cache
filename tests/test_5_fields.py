from caches.AshedCacheCompiled import AshedCacheCompiled
from CacheTest import do_test
from utilities.Plot import do_plot
from caches.AshedCache import AshedCache


# the name of fields
from utilities.PupulateCache import *

KEY_FIELDS = ['A', 'B', 'C', 'D', 'E']

# Define the distribution of rules with 1, 2, 3, 4, and 5 keys
key_distribution = {
    1: 0.01,  # 1% of rules will have 1 key
    2: 0.02,  # 2% of rules will have 2 keys
    3: 0.02,  # 2% of rules will have 3 keys
    4: 0.15,  # 15% of rules will have 4 keys
    5: 0.80   # 80% of rules will have 5 keys
}
# the max integer that can be used as value for any of the key
max_int = 100

results = {}

# populate_cache = PopulateCache(max_int, KEY_FIELDS, key_distribution)
for n in [1,10,100,500,1000,2500,5000]:
    cache = AshedCache()
    ashed = do_test(cache,num_records=n)

    cache = AshedCacheCompiled()
    compiled = do_test(cache,num_records=n)
    results[n] = (ashed,compiled)

print(results)
do_plot(results, 'Average Search Time vs Number of Rules. 5 key fields')