from caches.AshedCacheCompiled import AshedCacheCompiled
from CacheTest import do_test
from caches.AshedCacheCompiledSmart import AshedCacheCompiledSmart
from constants import KEY_FIELDS
from utilities.Plot import do_plot
from caches.AshedCache import AshedCache

results = {}

# populate_cache = PopulateCache(max_int, KEY_FIELDS, key_distribution)
for n in [1, 10, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500]:
    cache = AshedCache()
    ashed = do_test(cache, num_records=n)

    cache = AshedCacheCompiled()
    compiled = do_test(cache, num_records=n)

    cache = AshedCacheCompiledSmart()
    smart = do_test(cache, num_records=n)

    results[n] = (ashed, compiled, smart)

print(results)
do_plot(results, 'Average Search Time vs Number of Rules. '+str(len(KEY_FIELDS))+' key fields')
