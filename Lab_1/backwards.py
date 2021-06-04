def backwards(s, index=-1):
    """returns a string in reverse!
    * Using recursion and no comprehensions
    * Goes backwards via indexing, eg -1, -2, -3, -4, -5"""
    if len(s) == 0 or -index-1 == len(s):
        # stops the recursion, if the index has reached the start of the string
        return ''
    else:
        return s[index] + backwards(s, index-1)