class Item:
    """An item to (maybe) put in a knapsack"""

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item({self.value}, {self.weight})"


def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
    table = [(capacity+1) * [0] for num in range(len(items)+1)]
    items_used = []
    # Loop through all the possibilities, dont need to start at zero because when i=j=0, entries are zero anyways
    for i in range(1, len(items)+1):
        # Get the current item that we are dealing with, easier to store as obj instead of indexing items each time
        curr_item = items[i-1]
        # Go through every capcacity for this item
        for j in range(1, capacity+1):
            # Check to see if the curr_item can even fit in the knapsack, if not, dont use it
            if (curr_item.weight > j):
                # NB if this line wasnt here, indexing bellow would wrap around to the end of the table
                table[i][j] = table[i-1][j]
            # Otherwise curr_item can fit in the knapsack, take the largest value from not taking it vs taking it
            else:
                value_dontUse_curr_item = table[i-1][j]
                value_use_curr_item = table[i-1][j-curr_item.weight]+curr_item.value
                table[i][j] = max(value_dontUse_curr_item, value_use_curr_item)
    #return table[-1][-1]
    return knapsack_back_track(table, items, capacity)

def knapsack_back_track(table, items, capacity):
    j = capacity
    i = len(items)
    items_used = []
    while i > 0 and i > 0:
        if table[i][j] != table[i-1][j]:
            # Item was added to the back pack, as capacity dicates it
            j -= items[i-1].weight
            items_used.append(items[i-1])
        i -= 1
    return items_used


# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
print(max_value(items, 10))
