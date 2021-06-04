def fib(n, matrix=None):
    """finds the nth fibonacci sequence using divide and conquer and
    fast exponentiation"""
    #how to use martix multiplication in python??
    #how can i implement 2x2 matrix multiplicatoin in python, look at the general formula.
    # fib matrix = [[fn+1, fn], [fn, fn-1]]
    if n == 1 or n==2:
        return 1
    else:
        fib_matrix = matrix_power_rec( [[1, 1], [1, 0]] , n) #helper does much of the work
        fib_n = fib_matrix[0][1] # or fib_matrix[1][0], doesnt matter
        return fib_n


def matrix_power_rec(matrix, n):
    """computes a matrix to a power using the power of recursion,
    only works for a 2x2 matrix!
    takes matrix in form [[topLeft, topRight],[bottomLeft, bottomRight]]"""
    if n==0 or n==1:
        return matrix
    else:
        result = matrix_power_rec(matrix, n//2)
        # Square the result matrix
        top_left = result[0][0]*result[0][0] + result[0][1]*result[1][0]
        top_right = result[0][0]*result[0][1] + result[0][1]*result[1][1]
        bottom_left = result[1][0]*result[0][0] + result[1][1]*result[1][0]
        bottom_right = result[1][0]*result[0][1] + result[1][1]*result[1][1]
        power_matrix = [[top_left, top_right], [bottom_left, bottom_right]]
        if n%2==0:
            return power_matrix
        else: # n is odd
            top_left_o = matrix[0][0]*power_matrix[0][0] + matrix[0][1]*power_matrix[1][0]
            top_right_o = matrix[0][0]*power_matrix[0][1] + matrix[0][1]*power_matrix[1][1]
            bottom_left_o = matrix[1][0]*power_matrix[0][0] + matrix[1][1]*power_matrix[1][0]
            bottom_right_o = matrix[1][0]*power_matrix[0][1] + matrix[1][1]*power_matrix[1][1]
            return [[top_left_o, top_right_o], [bottom_left_o, bottom_right_o]]