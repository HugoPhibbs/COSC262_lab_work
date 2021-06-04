from collections import defaultdict

def change_greedy(amount, coinage):
    result = []
    counts = defaultdict(int);
    remaining = amount
    coinage.sort()
    coinage.reverse()
    i = 0
    max_coin = coinage[i]
    while remaining > 0:
        if max_coin <= remaining:
            counts[max_coin] += 1
            remaining -= max_coin
        else:
            i += 1
            if i == len(coinage):
                return None
            max_coin = coinage[i]
    for j in range(len(coinage)):
        coin = coinage[j]
        if counts[coin] > 0:
            result_tuple = (counts[coin], coinage[j])
            result.append(result_tuple)
    return result




print(change_greedy(82, [10, 25, 5]))