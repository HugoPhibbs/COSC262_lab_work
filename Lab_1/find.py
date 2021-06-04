def find(data, value, index=0):
    """returns the first instance of value in a list, or -1 if the value is not found
    * Using recursion, with no comprehensions"""
    if index==len(data):
        return -1
    else:
        if data[index]==value:
            return index
        else:
            return find(data, value, index+1)