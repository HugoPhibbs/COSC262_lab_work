def product(data, index=0):
    """returns the product of everything in data"""
    if len(data) == 0 or index == len(data):
        return 1
    else:
        return data[index] * product(data, index+1)