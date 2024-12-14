def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    a_str = list(str(x))

    is_negative = 1

    if a_str[0] == "-":
        is_negative = -1
        a_str = a_str[1:len(a_str)]

    a_str.reverse()

    return_num = int("".join(a_str))

    return is_negative * return_num

print(reverse(-5684300))