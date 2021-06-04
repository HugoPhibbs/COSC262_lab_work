def concat_list(strings, index=0):
    """turns a bunch of strings into a list"""
    if len(strings) == 0 or index == len(strings):
        return ''
    else:
        return strings[index]+concat_list(strings, index+1)