def is_strongly_connected(adj_list):
    """takes a graph and returns True if the graph is strongly connected, otherwise False"""
    # First check if the graph before transposing is strongly connected
    adj_list_bfs = bfs_tree(adj_list, 0)
    if adj_list_bfs.count(None) > 1:
        # Not strongly connected
        return False
    # Now check the transpose graph
    trans_adj_list = transpose(adj_list)
    trans_adj_list_bfs = bfs_tree(trans_adj_list, 0)
    return (not trans_adj_list_bfs.count(None) > 1)


def bfs_tree(adj_list, start):
    """takes a graph in adj_list, does a BFS and returns the parent array"""
    length = len(adj_list)
    state_list = ["U"] * length
    parent_list = [None] * length
    queue = []  # Use a list as queue, back is enqueue, front is dequeue
    state_list[start] = "D"
    queue.append(start)  # Enqueue start to queue
    return bfs_loop(adj_list, queue, state_list, parent_list)


def bfs_loop(adj_list, queue, state_list, parent_list):
    """"does the main part of a BFS search"""
    while len(queue) != 0:
        current_node = queue.pop(0)  # Dequeue
        for edge_tuple in adj_list[current_node]:
            adj_node = edge_tuple[0]
            if state_list[adj_node] == "U":
                state_list[adj_node] = "D"
                parent_list[adj_node] = current_node
                queue.append(adj_node)
        state_list[current_node] = "P"
    return parent_list


def transpose(adj_list):
    """returns the transpose of a graph with the given adj_list"""
    trans_adj_list = [[] for i in range(len(adj_list))]
    for i in range(0, len(adj_list)):
        vertex_list = adj_list[i]
        for edge_tuple in vertex_list:
            edge_dest = edge_tuple[0]
            edge_weight = edge_tuple[1]
            trans_adj_list[edge_dest].append((i, edge_weight))
    return trans_adj_list