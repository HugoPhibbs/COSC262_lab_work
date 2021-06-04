def almost_all(numbers):
    """demonstration"""
    summed = sum(numbers)
    new_list = []
    for x in numbers:
        new_list.append(summed-x)
    return new_list