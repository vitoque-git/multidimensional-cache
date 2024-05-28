from caches.AshedCacheCompiled import AshedCacheCompiled
from CacheTest import do_test
from caches.AshedCacheCompiledSmart import AshedCacheCompiledSmart
from constants import KEY_FIELDS
from utilities.Plot import do_plot
from caches.AshedCache import AshedCache

results = {}

# populate_cache = PopulateCache(max_int, KEY_FIELDS, key_distribution)
for n in [1, 50, 100, 300, 500, 750, 1000, 1200, 1500]:
    cache = AshedCache()
    ashed, search_dataset1 = do_test(cache, num_records=n)
    data = cache.cache

    cache = AshedCacheCompiled()
    compiled, search_dataset2 = do_test(cache, data=data, search_dataset=search_dataset1)

    cache = AshedCacheCompiledSmart()
    smart, search_dataset3 = do_test(cache, data=data, search_dataset=search_dataset1)

    results[n] = (ashed, compiled, smart)

print(results)
do_plot(results, 'Average Search Time vs Number of Rules. ' + str(len(KEY_FIELDS)) + ' key fields')
