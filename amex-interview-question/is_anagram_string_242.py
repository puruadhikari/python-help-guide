from collections import Counter

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_cntr = Counter(list(s))
    t_cntr = Counter(list(t))
    return s_cntr==t_cntr


print((isAnagram("care","race")))