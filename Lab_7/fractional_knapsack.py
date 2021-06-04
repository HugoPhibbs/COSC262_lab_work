def fractional_knapsack(capacity, items):
    items_valued = []
    for (name, value, weight) in items:
        items_valued.append((name, value/weight, value, weight))
    # sort item for b/w in reverse
    items_valued = sorted(items_valued, key=lambda x: x[1])
    items_valued.reverse()
    result, i = 0, 0
    while capacity > 0:
        if i == len(items_valued): # dont assume that they all wont fit!
            return result
        curr_item = items_valued[i]
        curr_efficacy =  curr_item[1]
        curr_value = curr_item[2]
        curr_weight = curr_item[3]
        if curr_weight > capacity:
            ## add fractional parts of item
            fractional_value = (capacity/curr_weight) * curr_value
            result += fractional_value
            capacity = 0
        else:
            capacity -= curr_weight
            result += curr_value
        i += 1
    return result
    #take items in order of their value for money

# The example from the lecture notes
items = []
print(fractional_knapsack(9, items))