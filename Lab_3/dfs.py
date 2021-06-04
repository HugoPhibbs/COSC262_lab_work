def dfs_tree(adj_list, start):
    """"takes a graph in adj_list, does a DFS and returns the parent array"""
    length = len(adj_list)
    state_list = ["U"] * length
    parent_list = [None] * length
    state_list[start] = "D"
    dfs_loop(adj_list, start, state_list, parent_list)
    return parent_list

def dfs_loop(adj_list, current_node, state_list, parent_list):
    """does the main part for DFS search"""
    for edge_tuple in adj_list[current_node]:
        adj_node = edge_tuple[0]
        if state_list[adj_node] == "U":
            state_list[adj_node] = "D"
            parent_list[adj_node] = current_node
            dfs_loop(adj_list, adj_node, state_list, parent_list)
    state_list[current_node] = "P"