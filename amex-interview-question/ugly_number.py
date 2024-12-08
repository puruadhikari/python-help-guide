"""
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6."""


def nth_ugly_umber(n, a, b, c):
    number_set = set()

    for index in range(1, n + 1):
        number_set.add(a * index)
        number_set.add(b * index)
        number_set.add(c * index)

    number_list = list(number_set)
    number_list.sort()
    return number_list[n - 1]


print(nth_ugly_umber(n=4, a=2, b=3, c=4))
