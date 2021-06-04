def bfs_tree(adj_list, start):
    """takes a graph in adj_list, does a BFS and returns the parent array"""
    length = len(adj_list)
    state_list = ["U"]*length
    parent_list = [None]*length
    queue = [] # Use a list as queue, back is enqueue, front is dequeue
    state_list[start] = "D"
    queue.append(start) # Enqueue start to queue
    return bfs_loop(adj_list, queue, state_list, parent_list)

def bfs_loop(adj_list, queue, state_list, parent_list):
    """"does the main part of a BFS search"""
    while len(queue) != 0:
        current_node = queue.pop(0) # Dequeue
        for edge_tuple in adj_list[current_node]:
            adj_node = edge_tuple[0]
            if state_list[adj_node] == "U":
                state_list[adj_node] = "D"
                parent_list[adj_node] = current_node
                queue.append(adj_node)
        state_list[current_node] = "P"
    return parent_list