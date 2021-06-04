import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, index=0):
    """Takes a list of numbers and does weird stuff with it
    what my redisign does: use the same list over and over again,
    but instead of slicing, it tracks an index variable to know
    when to start"""
    if index == len(data): # Reached the end of the list
        # Returns 0 if the list is empty
        return 0
    else: # List is not empty O(n)
        if (data[index] // 100) % 3 != 0:
            return 1 + dumbo_func(data, index+1)
        else:
            return dumbo_func(data, index+1)