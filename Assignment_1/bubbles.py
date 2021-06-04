from Helpers import *


def bubbles(physical_contact_info):
    """finds the components of a graph, thus the bubbles for people to stay in
    mostly just taken the algorithm given in the lecture"""

    # Initialising variables
    adj_list = adjacency_list(physical_contact_info)
    length = len(adj_list)
    state = ["U"] * length
    queue = []
    parent_array = [None] * length
    components = []
    # Note that we don't need a set because things are only added if they arent duplicates anyways

    # Go through the the graph one vertex at a time with i
    for i in range(length):
        # i.e we haven't already one a BFS on this vertex
        if state[i] == "U":
            previous_state = state.copy()
            state[i] = "D"
            queue.append(i)
            bfs_loop(adj_list, queue, state, parent_array)
            new_component = []
            for j in range(length):
                # Can be a maximum of n components
                if state[j] != previous_state[j]:
                    # Ie if the previous BFS explored the same component as last time, don't need to add
                    # Checking which vertices have changed state
                    new_component.append(j)
            # How to find all the vertices that have changed state? use a forloop and compare?
            components.append(new_component)

    return components

physical_contact_info = """\
U 2
0 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

print('\n')

physical_contact_info = """\
U 2
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

print('\n')

physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

print('\n')


physical_contact_info = """\
U 0
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
print('\n')


physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))