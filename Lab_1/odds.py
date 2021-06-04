def odds(data, index=0):
    """takes a list of ints, and returns just the odd elements in a list"""
    if index==len(data):
        return []
    else:
        if data[index]%2!=0:
            return [data[index]]+odds(data, index+1)
        else:
            return odds(data, index+1)