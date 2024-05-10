"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

def josephus(int_list, skip):
    """
    Print every nth member while removing them in a circular fashion.

    :param int_list: list[int]: List of integers representing people sitting in a circular fashion.
    :param skip: int: Number of members to skip before removing the next one.
    :return: generator: Generator yielding the removed members.
    """
    skip = skip - 1                     # list starts with 0 index
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (skip + idx) % len_list   # hash index to every 3rd
        yield int_list.pop(idx)
        len_list -= 1
