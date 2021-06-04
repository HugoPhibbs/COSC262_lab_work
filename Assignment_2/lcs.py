def lcs(s1, s2):
    """"Finds the longest common subsequence using bottom up DP"""
    n_cols = len(s2)
    n_rows = len(s1)
    table = [(n_cols+1) * [0] for i in range(n_rows+1)]

    # Create a table, going through the cols first and then the rows
    # Store the predecessor in the table, as a tuple pair

    for i in range(n_rows+1):
        for j in range(n_cols+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    back_track = back_track_lcs_iter(table, s1, s2)
    back_track.reverse()
    return "".join(back_track)


def back_track_lcs_iter(table, s1, s2):
    """finds the result of a LCS of s1 and s2 using iteration to backtrack a table"""
    done = False
    i = len(table) - 1
    j = len(table[0]) - 1
    result = []
    while not done:
        if i == 0 or j == 0:
            done = True
        elif s1[i-1] == s2[j-1]:
            result.append(s1[i-1])
            i -= 1
            j -= 1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1
    return result


def back_track_lcs_rec(table, s1, s2, i=None, j=None):
    """Back tracks through a table to build a solution to the longest common subsequence
    results a list of an LCS """
    if i is None:
        i = len(table)-1
        j = len(table[0])-1
    if i == 0 or j == 0:
        return []
    if s1[i-1] == s2[j-1]:
        return [s1[i-1]] + back_track_lcs_rec(table, s1, s2, i-1, j-1)
    else:
        if table[i-1][j] > table[i][j-1]:
            return back_track_lcs_rec(table, s1, s2, i-1, j)
        else:
            return back_track_lcs_rec(table, s1, s2, i, j-1)
