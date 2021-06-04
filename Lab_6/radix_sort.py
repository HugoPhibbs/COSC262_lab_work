from couting_sort_all import *

def radix_sort(numbers, d):
    for i in range(1, d+1):
        key = lambda x: int(('0'*(i - len(str(x)))+str(x))[-i])
        numbers = counting_sort(numbers, key)
    return numbers

