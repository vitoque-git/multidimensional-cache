from abc import ABC, abstractmethod

class MultiDimensionalCacheBase(ABC):
    @abstractmethod
    def add_to_cache(self, params, value):
        pass

    @abstractmethod
    def search_cache(self, params):
        pass