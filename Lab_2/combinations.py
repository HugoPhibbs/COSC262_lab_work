def combinations(items, r, candidate=None, result=[]):
    if candidate is None:
        candidate = ()
    if is_solution(candidate, r):
        result.append(candidate)
    else:
        for i in range(r-1):
            child = children(items[i:], (items[i],))
            print(child)
    return result
        # Create it's children and return them


def children(items, candidate):
    """Returns the children for a given candidate"""
    children = []
    for item in items:
        if item not in candidate:
            candidate_copy = candidate + (item,)
            children.append(candidate_copy)
    return children

def is_solution(candidate, r):
    return len(candidate) == r


print(combinations([1, 2, 3, 4],3))