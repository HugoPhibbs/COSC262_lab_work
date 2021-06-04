import sys

sys.setrecursionlimit(2000)


class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"

def max_value(items, capacity, cache=None, n=None):
    """find the max possible val fitting things in a knapsack using dp"""
    ## using top town, so use a cache to only find the values that we need

    # item has form value, weight
    if cache is None:
        cache = {}
    if n is None:
        n = len(items)
    if (n, capacity) in cache:
        return cache[(n, capacity)]
    # When there is no more items to add
    if n==0:
        return 0
    # Top item is too heavy to fit
    elif items[n-1].weight > capacity:
        return max_value(items, capacity, cache, n-1)
    else:
        # Not using the last value
        max_val = max(max_value(items, capacity, cache, n-1), items[n-1].value + max_value(items, capacity-items[n-1].weight, cache, n-1))
        # Using the last value
        cache[(n, capacity)] = max_val
        return max_val

items = [()]