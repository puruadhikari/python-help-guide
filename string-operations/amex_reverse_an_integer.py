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


def reverse_integer(val):
    result = 0
    is_nagetive = False

    if val < 0:
        is_nagetive = True
        val = -1 * val

    while val // 10 > 0:
        bal = val // 10
        reminder = val % 10
        result = result * 10 + reminder * 10
        val = bal

    if is_nagetive:
        return -1 * (result + bal)

    return result + bal


print(reverse_integer(-5684300))

print(reverse(-5684300))