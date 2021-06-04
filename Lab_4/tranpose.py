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