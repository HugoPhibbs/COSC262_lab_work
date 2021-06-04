def all_pairs(list1, list2, index=0):
    """finds the pairs of tuples that can be created with two lists
    done recursively
    goes through list 1 against 2"""
    if index == len(list1) - 1:
        return all_pairs_help(list1[index], list2)

    else:
        return all_pairs_help(list1[index], list2) + all_pairs_help(list1[index + 1], list2)


def all_pairs_help(list1_el, list2, index=0):
    """Helper function for above"""
    if index == len(list2) - 1:
        return [(list1_el, list2[index])]
    else:
        return [(list1_el, list2[index])] + all_pairs_help(list1_el, list2, index + 1)