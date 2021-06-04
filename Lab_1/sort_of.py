def sort_of(numbers):
    """docstring
    formula for appearences = (og_position+1)-length(result)"""
    result_list = [None] * len(numbers)
    if len(numbers)==0:
        return result_list
    min_number = numbers[-1]
    result_list[-1] = min_number
    for i in range(1, len(numbers)+1):
        if numbers[-i] < min_number:
            min_number = numbers[-i]
            result_list[-i] = min_number
        else:
            result_list[-i] = min_number
    return result_list
