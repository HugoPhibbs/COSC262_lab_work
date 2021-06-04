# Do not alter the next two lines
from collections import namedtuple

Node = namedtuple("Node", ["value", "left", "right"])


# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False, start=None, end=None):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
    n = len(nums)
    if n == 1:
        tree = Node(nums[0], None, None)  # A leaf
    else:
        end = n // 2  # Halfway (approx)
        left = binary_search_tree(nums[start:end], start, end)
        right = binary_search_tree(nums[end: ]      , end, end)
        tree = Node(nums[mid - 1], left, right)
    return tree


# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None:  # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)
