from caches.AshedCache import AshedCache
from caches.AshedCacheCompiled import AshedCacheCompiled
import types

class AshedCacheCompiledSmart(AshedCacheCompiled):

    def compile_patterns(self):
        # calculate as usual the patterns
        super().compile_patterns()

        # If all patterns are valid, set the generate_keys method to point to the AshedCache.generate_keys method
        if all(self.matching_pattern.values()):
            # Replace generate_keys method with super().generate_keys
            self.generate_keys = types.MethodType(AshedCache.generate_keys(self, params))


