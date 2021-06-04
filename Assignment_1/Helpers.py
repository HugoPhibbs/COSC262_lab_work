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


def adjacency_list(graph_str):
    """returns the adj list of a graph from a textual representation
    adj list has edges of a vertex, along with edge weight
    in form (destination, weight)"""

    # Isolate the top row of graph str, and create a list
    info_string = graph_str[:graph_str.index('\n')]
    info_list = info_string.split(" ") # Seperates graph str into
    weighted = (info_list[-1]=="W") # Find whether graph is weighted
    directed = (info_list[0]=="D") # Find whether graph is directed
    adj_list = [[] for i in range(int(info_list[1]))]  # Create adj list

    # Split the graph into lines, then process each line differently
    # small list from each line, up to 3 elements long.
    # First item in small list is source, second is destination, third is weight (if any)

    # Create an edge list from str
    edge_list = graph_str[graph_str.index("\n")+1:-1].split("\n")
    if edge_list == ['']:
        return adj_list

    # Iterate through each edge
    for edge in edge_list:
        edge_info = edge.split(' ')
        source = int(edge_info[0])
        dest = int(edge_info[1])
        weight = None
        if weighted:
            weight = int(edge_info[-1])
        # Add source-dest edge, this is always done
        edge_tuple_source = (dest, weight)
        adj_list[source].append(edge_tuple_source)
        if not directed: # Add dest-source edge, only done for undirected graphs
            edge_tuple_dest = (source, weight)
            adj_list[dest].append(edge_tuple_dest)
    return adj_list


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