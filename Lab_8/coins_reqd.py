def coins_reqd(value, coinage):
    """A version that doesn't use a list comprehension"""
    # uses a bottom up aproach

    # Change it so it returns of tuples of coins, and how many times they were used
    # in form [(denomination, num_coins)]

    # num coins holds a list for the number of coins required for every value that could be asked
    # from the lecture notes, this is what it is doing.
    numCoins = [(0, 0) for i in range(value+1)] # Holds (coins, predeccesor)

    # Go through all the possible amt values up to the one that we want.
    # Note that this starts from one, because the num coins reqd for 0 is 0
    for amt in range(1, value + 1):
        # Create a minimum value
        minimum = float("inf")
        pred = None
        # Go through all the coins in coinage, and take them away from amt if you coin
        for coin in coinage:
            # Able to take off this current coin
            if amt >= coin:
                # Get the value associated with jumping back the coin.
                coin_count = numCoins[amt - coin][0]  # Num coins required to solve for amt - c
                curr_pred = amt-coin
                # This line is key, go through all the coins in the coinage, Trying to take them off for every amount
                # up to the value that you want.
                # Ie by taking this current coin off the value, what is the leasy amount of coins to express this new value
                # This creates a somewhat recursive nature to the entire thing.
                #
                # EG. Say we had a coinage {1, 5, 10, 15}
                # and at the current point in time we have numCoins (coinsReqd, amount)
                # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (1, 10), (??, 11)]
                #
                # Say we wanted to find the number of coins required for the amount of 11. So what could we do
                # Since 15>11, we cant use that, but we can use all the other remaining coins {1, 5, 10}
                #
                # So lets take each of the coins off and see what the minimum coins required for this new amt created
                # from taking this coin off.
                #
                # Remember numCoins is in format (coinsReqd, amount)
                # Take off 10, we reach in num coins (1, 1)  -- So 1 more coin(s) required to express the value of 11
                # Take off 5, we reach in num coins (2, 6)   -- So 2 more coin(s) required to express the value of 11
                # Take off 1, we reach in num coins (1, 10)  -- So 1 more coin(s) required to express the value of 11
                #
                # So this is quite a boundary case actually, didnt mean to get it like this!!
                # However taking 10, 5 and 1 off, we find that the min coins reqd from taking a coin off belongs to 1
                # or 10, we can pick either. Will pick 10, becuase it goes from largest to smallest.
                if coin_count < minimum:
                    minimum = coin_count
                    pred = curr_pred
        # So then once we have found the minimum from taking off this particular coin. In the particular amt in the table
        # add one to it (taking off a particular coin) and the minimum coins reqd to reach this amt.
        numCoins[amt] = (1 + minimum, pred)

    # Back track through the table to find the coins required for every amount

    coins_used = [] # Holds a tuples of (coin, times_used)
    rem_amt = value
    prev_coin_used = None # (Coin, times) used

    while rem_amt > 0:
        coin_used = rem_amt - numCoins[rem_amt][1]
        if prev_coin_used is None:
            prev_coin_used = (coin_used, 1)
        elif coin_used != prev_coin_used[0]:
            # Now using a new coin
            coins_used.append(prev_coin_used)
            prev_coin_used = (coin_used, 1)
        else:
            prev_coin_used = (prev_coin_used[0], prev_coin_used[1]+1)
            # Already used this coin before so add it to tuple
        # Algorithm will add a particular coin until it is no longer efficient, it wont just take it a time,
        # then use it later, coins used will always descent in size

        rem_amt -= coin_used
    if prev_coin_used is not None:
        coins_used.append(prev_coin_used)
        coins_used = sorted(coins_used, key=lambda x: x[0])
        coins_used.reverse()
    return coins_used

coinage = [1, 7, 11, 13, 29, 80, 97]
coinage_copy = coinage[:]
for amount in range(200):
    answer = coins_reqd(amount, coinage)
    ok, error = check_answer(amount, coinage, coinage_copy, answer)
    if not ok:
        print("Failed with amount =", amount)
        print(error)
        break

if ok:
    print("OK")