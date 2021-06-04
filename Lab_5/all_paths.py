def all_paths(adj_list, source, dest):
    path_list = []
    dfs_backtrack_ap((source,), adj_list, path_list, dest)
    return path_list

def dfs_backtrack_ap(path, adj_list, path_list, dest):
    if is_solution_ap(path, dest):
        add_to_output(path, path_list)
    else:
        # input_data[i] is the adj vertices for a particular vertex
        # children to a path should be the available vertices from
        # the last vertex in the path
        chosen_vertex = path[-1]
        for possible_path in children_ap(path, adj_list[chosen_vertex]):
            dfs_backtrack_ap(possible_path, adj_list, path_list, dest)


def is_solution_ap(path, dest):
    """Returns True if the candidate is complete solution"""
    # Complete the code
    # is a solution if the last vertex in path is the destination vertex
    return (path[-1] == dest)


def children_ap(path, adj_vertices):
    """Returns a collection of candidates that are the children of the given
    candidate."""
    possible_paths = []
    for edge_pair in adj_vertices:
        #Copy candidate tuple
        adj_vertex = edge_pair[0]
        temp_path = path + tuple()
        if adj_vertex not in path:
            temp_path += (adj_vertex,)
            possible_paths.append(temp_path)
    return possible_paths;
    # Complete the code

def add_to_output(candidate, output_data):
    output_data.append(candidate)

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

