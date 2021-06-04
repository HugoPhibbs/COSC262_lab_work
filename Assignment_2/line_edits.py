from lcs import lcs


def line_edits(s1, s2):
    """Finds the edit distance for lines given two input strings"""
    # split the inputted strings into two lists containing strings for each list
    s1_list = s1.split("\n")[:-1]
    s2_list = s2.split("\n")[:-1]
    table = edit_distance(s1_list, s2_list)
    actions = backtrack_edit_distance_iter(table, s1_list, s2_list)
    return actions


def edit_distance(s1_list, s2_list):
    """Creates a table for the edit distance between two input strings."""
    n_rows = len(s1_list)
    n_cols = len(s2_list)
    table = [(n_cols+1) * [0] for i in range(n_rows+1)]
    for i in range(n_rows+1):
        for j in range(n_cols+1):
            if i == 0 and j == 0:
                table[i][j] = 0
            elif j == 0:
                table[i][j] = i
            elif i == 0:
                table[i][j] = j
            elif s1_list[i-1] == s2_list[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
    return table


def backtrack_edit_distance_iter(table, s1_list, s2_list):
    """finds operations needed for editing a string s1 into s2"""

    done, actions = False, []
    i, j = len(s1_list), len(s2_list)

    while not done:
        # Since we are indexing the strings with i-1, or j-1, stop when i or j is less than 1
        # Check if the last char of the two strings is equal
        if (j == 0 and i == 0) or (i < 0) or (j < 0):
            done = True
        # Reached if we have reached the top row of the table
        elif i == 0:
            actions.append(("I", '', s2_list[j - 1]))
            j -= 1
        # Check if we have reached the far left of the table
        elif j == 0:
            actions.append(("D", s1_list[i - 1], ''))
            i -= 1
        # Current two letters are the same
        elif s1_list[i-1] == s2_list[j-1]:
            actions.append(("C", s1_list[i-1], s2_list[j-1]))
            i -= 1
            j -= 1
        # Otherwise check spots respective of deletion, insertion and substitution
        else:
            # Substitution
            # print(i, j)
            if table[i-1][j-1] <= table[i][j-1] and table[i-1][j-1] <= table[i-1][j]:
                str1, str2 = substitute_letters(s1_list[i-1], s2_list[j-1])
                min_option = ("S", str1, str2)
                i -= 1
                j -= 1
            # Deletion
            elif table[i-1][j] <= table[i][j-1] and table[i-1][j] <= table[i-1][j-1]:
                min_option = ("D", s1_list[i-1], '')
                i -= 1
            # Insertion
            elif table[i][j-1] <= table[i-1][j] and table[i][j-1] <= table[i-1][j-1]:
                min_option = ("I", '', s2_list[j-1])
                j -= 1
            actions.append(min_option)
    actions.reverse()
    return actions


def substitute_letters(str1, str2):
    """Returns a tuple of two strings Str1, and Str2 with
     characters highlighted that arent in the LCS of str1 and str2"""
    lcs_string = lcs(str1, str2)
    str1_result = substitute_letters_helper(str1, lcs_string)
    str2_result = substitute_letters_helper(str1, lcs_string)
    return str1_result, str2_result


def substitute_letters_helper(str, lcs_string, str_result=''):
    for i in range(len(str)):
        if str[i] in lcs_string:
            str_result += str[i]
        else:
            str_result += "[[{}]]".format(str[i])
    return str_result





# Test cases

s1 = "Line1\n"
s2 = ""
table = line_edits(s1, s2)
# Needs to be a single delete from s1 to s2
for row in table:
    print(row)

print()

s1 = "Line1\nLine3\nLine5\n"
s2 = "Twaddle\nLine5\n"
table = line_edits(s1, s2)
#('D', 'Line1', '')
#('S', 'Line3', 'Twaddle')
#('C', 'Line5', 'Line5')

for row in table:
    print(row)

print()

s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line5\nLine4\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)

print()

s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
table = line_edits(s1, s2)
for row in table:
    print(row)

print()

s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)