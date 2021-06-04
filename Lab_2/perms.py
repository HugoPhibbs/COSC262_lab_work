def perms(input_list, perm_tuple=(), result_list=None):
    """does the actual permumations part"""
    if len(input_list) == 1 and result_list is None:
        return [(input_list[0],)]
    if result_list is None:
        result_list = []
    if len(input_list) == 0:
        # This is just a base case for the quiz, kinda useless
        return [()]
    elif len(input_list) == 1:
        chosen = input_list.pop()

        perm_tuple += (chosen,)

        result_list.append(perm_tuple)
        return perm_tuple
    else:
        for i in range(0, len(input_list)):
            chosen = input_list[i]

            perm_tuple += (chosen,)

            # Copy the list, and then pop from this copied list
            sub_list = input_list.copy()
            sub_list.pop(i)

            perms(sub_list, perm_tuple, result_list)
            perm_tuple = perm_tuple[:-1]  # reset tuple to what it looked like before i
    return result_list