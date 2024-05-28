from caches.AshedCache import AshedCache
from caches.AshedCacheCompiled import AshedCacheCompiled


class AshedCacheCompiledSmart(AshedCacheCompiled):
    def __init__(self):
        super().__init__()
        self.use_compiled = False

    def generate_keys(self, params):
        """
        Generate all possible keys with decreasing number of parameters.
        """
        if self.use_compiled:
            return super().generate_keys(params)  # Call generate_keys from AshedCacheCompiled
        else:
            return AshedCache.generate_keys(self, params)  # Call generate_keys from AshedCache


    def compile_patterns(self):
        super().compile_patterns()

        for value in self.matching_pattern.values():
            if not value:
                self.use_compiled = True
                return

        self.use_compiled = False


