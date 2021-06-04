def my_enumerate(items, index=None):
    """"returns enumerate, recursively, starting from the front of the list"""
    if index is None:
        index = 0
    if len(items)==0:
        return []
    elif index == len(items)-1:
        # Reached the end of the list
        return [(index, items[index])]
    else:
        return [(index, items[index])] + my_enumerate(items, index+1)
