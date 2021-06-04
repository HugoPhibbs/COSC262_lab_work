def next_vertex(in_tree, distance):
    """returns the vertex that should be next added to the tree"""
    # Set the current bench mark for smallest distance,
    # and also set the first place to look in search
    min_index = in_tree.index(False)
    for i in range(min_index+1, len(in_tree)):
        # If the element isnt already in the tree (confirmed) in,
        # and it has the smallest weight, add it!
        if (in_tree[i] is False) and (distance[i] < distance[min_index]):
            min_index = i
    return min_index