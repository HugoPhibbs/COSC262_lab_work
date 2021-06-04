def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)


def is_solution(candidate, input_data):
    """Returns True if the candidate is complete solution"""
    # Complete the code
    return (len(candidate) == len(input_data))


def children(candidate, input_data):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    children = []
    for val in input_data:
        #Copy candidate tuple
        temp_cand = candidate + tuple()
        if val not in candidate:
            temp_cand += (val,)
            children.append(temp_cand)
    return children;
    # Complete the code

def add_to_output(candidate, output_data):
    output_data.append(candidate)


def should_prune(candidate):
    return False

perms = permutations(set())
print(len(perms) == 0 or list(perms) == [()])