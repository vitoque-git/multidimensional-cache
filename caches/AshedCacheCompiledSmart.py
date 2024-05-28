from caches.AshedCache import AshedCache
from caches.AshedCacheCompiled import AshedCacheCompiled
import types

class AshedCacheCompiledSmart(AshedCacheCompiled):

    def compile_patterns(self):
        # calculate as usual the patterns
        super().compile_patterns()

        # If all patterns are valid, fall back to the AshedCache class
        if all(self.matching_pattern.values()):
            self.__class__ = AshedCache


