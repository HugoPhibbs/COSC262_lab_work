def dijkstra(adj_list, next_node):
    """does dijkstras algorithm on a graph"""

    parent_array = [None for i in range(0, len(adj_list))]
    distance_array = [float('inf') for i in range(0, len(adj_list))]
    in_tree = [False for i in range(0, len(adj_list))]
    distance_array[next_node] = 0

    true_array = [True for i in range(0, len(adj_list))]

    while in_tree != true_array:
        # go throught the entire one vertex at a time,
        # if a vertex has been fully discovered, add its smallest edge to the parent array
        # go to the added vertex, and then add its edges.
        # then look at the total list of distance and the edges, and add the smallest one.
        # for the smallest one that is added, repeat this, until the in_tree is all done.

        # What to do with disconnected graphs?

        # add all adj edges with their weights to distance array
        u = next_vertex(in_tree, distance_array)
        in_tree[u] = True
        for (v, weight) in adj_list[u]:
            if not in_tree[v] and distance_array[u] + weight < distance_array[v]:
                distance_array[v] = distance_array[u] + weight
                parent_array[v] = u
    return parent_array, distance_array
    # hasnt yet discovered an adjacent vertex for current node


def next_vertex(in_tree, distance):
    """returns the vertex that should be next added to the tree"""
    # Set the current bench mark for smallest distance,
    # and also set the first place to look in search
    min_index = in_tree.index(False)
    for i in range(min_index + 1, len(in_tree)):
        # If the element isnt already in the tree (confirmed) in,
        # and it has the smallest weight, add it!
        if (in_tree[i] is False) and (distance[i] < distance[min_index]):
            min_index = i
    return min_index