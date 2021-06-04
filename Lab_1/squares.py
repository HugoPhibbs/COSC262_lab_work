def squares(data, index=0):
    """returns the squares of numbers in list data
     * Using recursion and no comprehensions"""
    if index==len(data):
        return []
    else:
        return [data[index]**2] + squares(data, index+1)