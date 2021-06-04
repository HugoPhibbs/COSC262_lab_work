"""A program to read a grid of weights from a file and compute the
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards.
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
INFINITY = float('inf')


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


def grid_cost1(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    # **** Your code goes here. It must compute a value 'best', which is
    # the minimum cost from the top of the grid to the bottom.

    # Do this without any recursion

    # Note for tabulation we dont need all the other values, only the ones that we need.

    table = [n_cols * [(0, 0)] for row in range(n_rows)]
    for i in range(n_rows):
        # i is the number of rows
        for j in range(n_cols):
            # j is the number of cols
            if i == 0:
                # First row
                table[i][j] = grid[i][j] -1
                done = True
            elif j == 0:
                # On the left edge of the table
                # Check above and to the right
                neighbours_sorted = sorted([(table[i-1][j], j), (table[i-1][j+1], j+1)], key=lambda x: x[0])
            elif j == n_cols-1:
                # On the right edge of the table
                neighbours_sorted = sorted([(table[i-1][j], j), (table[i-1][j-1], j-1)], key=lambda x: x[0])
            else:
                # Not on the edges
                # Check above, right and left
                neighbours_sorted = sorted([(table[i-1][j], j), (table[i-1][j-1], j-1), (table[i-1][j+1], j+1)], key=lambda x:x[0])
            if not done:
                min_neighbour, min_neighbour_col = neighbours_sorted[0][0], neighbours_sorted[0][1]
                table[i][j] = (table[i][j][0] + min_neighbour, min_neighbour_col)
    return min(table[n_rows-1][n_cols-1][0])

def min_cost_backtrack(table, j=None, i=None):
    # Find the cheapest entry on the bottom row
    if i and j == None:
        i = len(table)-1
        j = len(table)-1
    else:
        if (i, j) == (len(table)-1, len(table)-1):
            new_j = sorted(table, key=lambda x: x[0]) # Min col at the bottom row
            # Start the recursion at the bottom of the table
        else:
            new_j = table[i][j][1] # Get the predesscor for the current cell
            curr_cost = 90
            # Find the predescor the current cell
        # Find the minimum spot for the top, left and right cells




def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    # **** Your code goes here. It must compute a value 'best', which is
    # the minimum cost from the top of the grid to the bottom.

    # Do this without any recursion

    # Note for tabulation we dont need all the other values, only the ones that we need.

    table = [n_cols * [0] for row in range(n_rows)]
    for i in range(n_rows):
        # i is the number of rows
        for j in range(n_cols):
            # j is the number of cols
            if i == 0:
                min_neighbour_w = 0
                # First row
            elif j == 0:
                # On the left edge of the table
                # Check above and to the right
                min_neighbour_w = min(table[i-1][j], table[i-1][j+1])
            elif j == n_cols-1:
                # On the right edge of the table
                min_neighbour_w = min(table[i-1][j], table[i-1][j-1])
            else:
                # Not on the edges
                # Check above, right and left
                min_neighbour_w = min(table[i-1][j], table[i-1][j-1], table[i-1][j+1])
            table[i][j] = grid[i][j] + min_neighbour_w
    return min(table[i])

print(grid_cost([[6, 7, 4, 7, 8], [7, 6, 1, 1, 4], [3, 5, 7, 8, 2], [2, 6, 7, 0, 2], [7, 3, 5, 6, 1]]))