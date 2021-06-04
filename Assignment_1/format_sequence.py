from Helpers import *


# Imports all that is needed for this, make sure to include functions with submission

def format_sequence(converters_info, source_format, destination_format):
    """finds a shortest path from a source vertex to another vertex, in terms
    of total edges traversed. uses Dijkstra's with a constant edge weight,
    so it constructs a parent array that is purely based on the minimal
    number of edges"""

    # Create an adj list
    adj_list = adjacency_list(converters_info)

    # Make all edges have a weight of 1, with an updated list loop
    for vertex in adj_list:
        for j in range(len(vertex)):
            vertex[j] = (vertex[j][0], 1)

    # Do Dijkstra's and initialise path array
    parent_array, distance_array = dijkstra(adj_list, source_format)
    i = destination_format
    path_array = [i]

    # Go through the parent and back track until you reach the parent
    while parent_array[i] is not None:
        i = parent_array[i]
        path_array.append(i)

    # Reverse path array, because it starts from the destination vertex
    path_array.reverse()

    # Check if the path_array has reached the source_format
    if path_array[0] != source_format:
        return "No solution!"

    # Otherwise ok, return parent_array
    return path_array
