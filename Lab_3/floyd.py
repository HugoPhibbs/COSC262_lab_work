def floyd(distance):
    """calculates the distance between every pair of vertices in a graph"""
    length = len(distance)
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

def distance_matrix(adj_list):
    """takes an adj list and turns it into a matrix with path weights """
    length = len(adj_list)
    dist_matrix = [[float('inf')] * length for i in range(length)]
    for i in range(length):
        dist_matrix[i][i] = 0
        for (dest, weight) in adj_list[i]:
            dist_matrix[i][dest] = weight
    return dist_matrix

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

import pprint

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))