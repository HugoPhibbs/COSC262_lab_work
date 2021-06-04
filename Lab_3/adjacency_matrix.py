def adjacency_matrix(graph_str):
    """Creates an adjacency matrix from a graph str, and returns to user
    note that a bunch of this code is borrowed from adjacency_list
    * Default weight for edges are 1"""

    # Isolate the top row of graph str, and create a matrix
    info_string = graph_str[:graph_str.index('\n')]
    info_list = info_string.split(" ") # Seperates graph str into
    weighted = (info_list[-1]=="W") # Find whether graph is weighted
    directed = (info_list[0]=="D") # Find whether graph is directed
    size = int(info_list[1])
    adj_matrix = [[0] * size for i in range(size)]
    if weighted:
        adj_matrix = [[None] * size for i in range(size)]

    # Create an edge list from str
    edge_list = graph_str[graph_str.index("\n")+1:-1].split("\n")
    if edge_list == ['']: #For a graph with no edges
        return adj_matrix

    # Iterate over graph edges
    for edge in edge_list:
        edge_info = edge.split(' ')
        source = int(edge_info[0])
        dest = int(edge_info[1])
        weight = 1
        if weighted:
            weight = int(edge_info[-1])
        # Store source-dest edge, this is always done
        adj_matrix[source][dest] = weight
        if not directed:
            # Store dest-source edge, only done for undirected graphs
            adj_matrix[dest][source] = weight
    return adj_matrix
