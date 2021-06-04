from sorted_array import *
from key_positions import *

def counting_sort(array, key):
    positions = key_positions(array, key)
    return sorted_array(array, key, positions)