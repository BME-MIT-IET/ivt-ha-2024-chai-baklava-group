"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""


# False == 0 is True
def move_zeros(array):
    """
    Move all zeros to the end of the array while preserving the order of other elements.

    Args:
        array (list): Input array.

    Returns:
        list: Modified array with zeros moved to the end.
    """
    result = []
    zeros = 0

    for i in array:
        if i == 0 and not isinstance(i, bool):
            zeros += 1
        else:
            result.append(i)
    result.extend([0] * zeros)
    return result


print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
