from Helpers import *


def min_capacity(city_map, depot_position):
    """does something complicated"""
    # What this comes down to is doing Dijkstra's from the depot_position, and finding
    # the vertex that is the max_distance away. then simple algebra can be done to find
    # the minimum amount of battery needed.
    adj_list = adjacency_list(city_map)
    parent_array, distance_array = dijkstra(adj_list, depot_position)
    distance_array_updated = []
    for val in distance_array:
        if isinstance(val, int):
            distance_array_updated.append(val)
        else:
            distance_array_updated.append(-1)
    max_distance = max(distance_array_updated)
    max_battery = int((3*12*max_distance)/0.8)
    return max_battery



city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))