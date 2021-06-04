def lcs(str1, str2, cache=None):
    """Finds the longest commmon subsequence between two strings using top down DP"""
    # Check if the cache is empty for the recurison, otherwise initialize it
    if cache is None:
        cache = {}
    # Check if a solution for this problem has already been found, so get it from the cache
    if (str1, str2) in cache:
        return cache[(str1, str2)]
    elif (str2, str1) in cache:
        return cache[(str2, str1)]
    # Check if both strings are empty
    if str1=='' or str2=='':
        return ''
    # Check if both string have the same last letter
    elif str1[-1] == str2[-1]:
        # We could use both + str1[-1] and + str2[-1], choose either
        return lcs(str1[:-1], str2[:-1], cache) + str1[-1]
    # Otherwise the two strings are not empty and they do not have the same last letter
    else:
        # Do recursion on taking the last letter off each and returining the best outcome
        soln1 = lcs(str1[:-1], str2, cache) # Take last letter off str1
        soln2 = lcs(str1, str2[:-1], cache) # Take last letter off str2
        # Check which recursive soln has the bigger length
        # And cache the one that does.
        if len(soln1) > len(soln2):
            cache[(str1, str2)] = soln1
            return soln1
        else:
            cache[(str1, str2)] = soln2
            return soln2


s1 = "Solidandkeen\nSolidandkeen\nSolidandkeen\n"
s2 = "Whoisn'tsick\nWhoisn'tsick\nWhoisn'tsick"
lcs = lcs(s1, s2)
print(lcs)
print(repr(lcs))