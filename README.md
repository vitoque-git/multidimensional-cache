# multidimensional-cache

## Overview
A general software problem is described by dictionary access in situation in which a number of keys can be used in a hirerchical order, where matching with the most number of fields take priority compared to the same positive search with a smaller degree of matched parameters. This is common for rules in which you fallback in wildcarded fields. 
For example on a three fields fruit cache, based on colour, acidity and size, a rule 1 can be defined for fruits that are yellow, below 1kg and acid (three fields pattern), another one, rule 2, for fruits that are yellow and acid (two fields seach), and another one, rule 3, for fruits that are acid, rule 4 fruits that are green, rule 5 fruits that are red (all one field search). So, a lemon will be interecepted by the rule 1,2,3 but rule 1 will be applied because it match on two fields, size and acidity, while a banana satisfies only rule 3, and an avocado none.

So a search for a three dimensional cache will look like a if-then-else tree in which the further we go, the less fields are checked 

    if cache_search(fruit.colour=X, fruit.acidity=Y, fruit.size=Z) ...
    elif cache_search(fruit.colour=X, fruit.acidity=Y) ...
    elif cache_search(fruit.acidity=Y, fruit.size=Z) ...
    elif cache_search(fruit.colour=X, fruit.size=Z) ...
    elif cache_search(fruit.colour=X) ...
    elif cache_search(fruit.acidity=Y) ...
    elif cache_search(fruit.size=Z) ..
    else: not found

## Hashed serialised caches
A generic and performan implementation of this cache serach is based on ashing by serialising a three dimensional key, in which a wildcard is used to represent the key in case of wildcard. 

Each cache_search is indexed, so it has a O(1) complexity, however, as the number of combination of fields is esponential, 2^n −1 nonwhere n is the number of fields. So the example above 3 fields yield 7 paths, 5 fields give us a 31 combinations of keys to check, where 10 fields will give us a 1023 combinations. So in itself checking each combination is going to slow the search down and we can see the complexity becoming (2^n −1) * O(1)
The lemon will be a hit at the first leaf, a banana will explore 5 while the avocado will check the whole 9 paths before is resolved in a no hit

## Data introspection
For slow moving rules, one approach, borrowed from the world of complex event processing, could be to use the data itslef to make the code dynamically efficient. The rule introspection in fact, give us clues of which rules, will never yield a match and which not, therefore it is not needed to explore this tree path. 

In other words, taking the example of before in which we had three rules based on 
- rule1: colour, acidity, size
- rule2: colour and acidity
- rule3: acidity
- rule4: colour
- rule5: colour

So, we can already exclude a number of cases from our checks:

    if TRUE and cache_search(fruit.colour=X, fruit.acidity=Y, fruit.size=Z) ...
    elif TRUE and cache_search(fruit.colour=X, fruit.acidity=Y) ...
    elif FALSE and cache_search(fruit.acidity=Y, fruit.size=Z) ...
    elif FALSE and cache_search(fruit.colour=X, fruit.size=Z) ...
    elif TRUE andcache_search(fruit.colour=X) ...
    elif FALSE and cache_search(fruit.acidity=Y) ...
    elif FALSE and cache_search(fruit.size=Z) ..
    else: not found

We therefore moved from 9 checks to 3.

The cost is, obvioulsy paid elsewhre, and specifically to determine which leave needs to be evaluated and which not (the FALSE and TRUE of the code above are obvioulsy a cached dictionary of boolean, called matching_pattern in the code), an operation we will call compilation. This high cost operation is dependent on data, so needs to be done when data changes, and tehrefore the approach suits problem in which rules are static but events are not. This is a typical use case of complex event process from which we can borrow the approach. 

## the code

The implementation in Python has two caches implementation:
- A pure hash driven approach, AshedCache
- A has key with compiled search, AshedCacheCompiled.

AshedCacheCompiled differs from a pure AshedCache by implementing a method to compile the matching_pattern dictionary of whihc leaf can be skipped altogether:

    def _compile_patterns(self, param_keys):
        """
        Check all possible combinations of the provided parameter keys to see if they
        match any rule in the cache. Cache the results.

        Parameters:
        param_keys (list): A list of parameter keys to check.
        """
        # Iterate over all lengths of combinations from the length of param_keys down to 1
        for i in range(len(param_keys), 0, -1):
            # Generate all combinations of param_keys of length i
            for combo in combinations(param_keys, i):
                # Check if the current combination matches any data in the cache
                has_matching_pattern = self.has_matching_data(combo)
                # Cache the result of whether this combination has matching data
                self.matching_pattern[combo] = has_matching_pattern


The matching_pattern is then used to skip searches altogther, by eliminating combinations of keys for arriving event that do not match any possible search of rules:

    def generate_keys(self, params):
        """
        Generate all possible keys with decreasing number of parameters.
        """
        keys = []
        param_keys = list(params.keys())
        for i in range(len(param_keys), 0, -1):
            for combo in combinations(param_keys, i):
                if self.matching_pattern[combo]:
                    key = tuple((k, params[k]) for k in combo)
                    # print(params,combo, keys)
                    keys.append(key)
        return keys


## results
As you would expect, the more rules, the less pattern can be exluded.
For a 5 fields index, 1000 rules will cover statistically all 31 combinations giving no advantage, while 100 will yiled only half of the combination, yileding a 100% improve of performance. Less than 100 rules, and the performance is more and more evident. 






  
