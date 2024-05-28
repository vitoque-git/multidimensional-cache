from caches.AshedCacheCompiled import AshedCacheCompiled
from CacheTest import do_test
from caches.AshedCacheCompiledSmart import AshedCacheCompiledSmart
from constants import KEY_FIELDS
from utilities.Plot import do_plot
from caches.AshedCache import AshedCache

results = {}

cache = AshedCache()
# cache = AshedCacheCompiled()
# cache = AshedCacheCompiledSmart()

do_test(cache, num_records=1000, num_iterations=1)


