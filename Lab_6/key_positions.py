def key_positions(seq, key):
    # var key is a key function for finding k

    key_array = []
    for num in seq:
        key_array.append(key(num))
    max_k = max(key_array)

    output_array = [0] * (max_k+1)

    for num in seq:
        output_array[key(num)] = output_array[key(num)] + 1
    summed = 0

    for i in range(max_k+1):
        output_array[i], summed = summed, summed+output_array[i]

    return output_array



