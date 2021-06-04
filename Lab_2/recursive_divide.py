def recursive_divide(x, y):
    """recursive division without using *, / or //
    return x//y"""
    if x>=y:
        return 1 + recursive_divide(x-y, y)
    else:
        return 0