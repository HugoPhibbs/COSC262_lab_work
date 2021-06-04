def cycle_length(n):
    """find the length of a collatz cycle using recursion"""
    if n == 1: # Base case
        return 1
    elif n%2==0: #Even:
        return 1 + cycle_length(n//2)
    else: # Odd
        return 1 + cycle_length(3*n+1)