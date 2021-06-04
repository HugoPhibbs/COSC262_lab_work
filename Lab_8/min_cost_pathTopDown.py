"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')  # Same as math.inf

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    # using our own cache, implemented with a dictionairy
    def cell_cost(row, col, cache=None):
        """The cost of getting to a given cell in the current grid."""
        # If the cache doesnt already exist, initialize it
        if cache is None:
            cache = {}
        # Check if wanted row and col is already in the table
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        # Check if our answer is already in the table, this is helpful as
        # you are envitably going to reach the same spot in the table with a normal traverse
        # in this way we are only calculating the cost of traversing to a spot only once, n
        # not multiple times!, the essence of DP!!!!!
        if (row, col) in cache:
            return cache[(row, col)]
        # If the spot in the table hasnt been logged yet, do a traversal on all it the min cost of all the
        # spots above it. (going from the top of the table)
        else:
            # Get the current cost assosiated with this spot, excluding traversals to this spot
            cost = grid[row][col]
            if row != 0: # Accounts for trivial case on the top row
                # Changed the range function bellow
                cost += min(cell_cost(row - 1, col + delta_col, cache) for delta_col in range(-1, +2))
            cache[(row, col)] = cost
            return cost

    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best


def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

print(file_cost('checkerboard.trivial.in'))
