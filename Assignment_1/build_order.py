from Helpers import *


def build_order(dependencies):
    """returns a topological ordering of a graph
    assume that the graph is always a DAG"""
    adj_list = adjacency_list(dependencies)
    length = len(adj_list)
    state_list = ["U"] * length
    parent_list = [None for j in range(length)]
    stack = []

    # Since the graph is Acyclic we can be sure that any DFS will produce a topological ordering
    for i in range(length):
        if state_list[i] == "U":
            dfs_loop_mod(adj_list, i, state_list, parent_list, stack)
    stack.reverse()
    return stack


def dfs_loop_mod(adj_list, current_node, state_list, parent_list, stack):
    """does the main part for DFS search"""
    for edge_tuple in adj_list[current_node]:
        adj_node = edge_tuple[0]
        if state_list[adj_node] == "U":
            state_list[adj_node] = "D"
            parent_list[adj_node] = current_node
            dfs_loop_mod(adj_list, adj_node, state_list, parent_list, stack)
    state_list[current_node] = "P"
    stack.append(current_node)


dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))