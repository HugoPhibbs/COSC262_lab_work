from Helpers import *


def which_segments(city_map):
    """does prims algorithm on a graph"""
    adj_list = adjacency_list(city_map)
    length = len(adj_list)
    in_tree_array = [False] * length
    distance_array = [float('inf')] * length
    parent_array = [None] * length
    distance_array[0] = 0  # Choose an arbitrary starting vertex
    true_array = [True] * length

    while in_tree_array != true_array:
        u = next_vertex(in_tree_array, distance_array)
        in_tree_array[u] = True
        for (v, weight) in adj_list[u]:
            if not in_tree_array[v] and weight < distance_array[v]:
                # If it hasn't been processed and we have
                # found a new smaller distance to the tree
                distance_array[v] = weight
                parent_array[v] = u
    # How to create a list of edge tuples from tree?

    edge_array = []
    for i in range(length):
        if parent_array[i] is None:
            continue
            # Found a parent
        else:
            edge_pair = [i, parent_array[i]]
            edge_tuple = tuple(sorted(edge_pair))
            edge_array.append(edge_tuple)
    return edge_array

city_map = """\
U 1 W
"""

print(sorted(which_segments(city_map)))