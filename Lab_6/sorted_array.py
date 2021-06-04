from key_positions import *

def sorted_array(seq, key, positions):
    key_pos_array = key_positions(seq, key)
    output_array = [0] * len(seq)
    for num in seq:
        output_array[key_pos_array[key(num)]] = num
        key_pos_array[key(num)] = key_pos_array[key(num)] + 1
    return output_array

