"""Find cross-list pairs that hit a target sum.

Args:
    arr1: First list of integers (converted to a set for lookup).
    arr2: Second list of integers.
    target: Desired sum.

Returns:
    List of tuples ``(a, b)`` where ``a`` is from ``arr1`` and ``b`` is from
    ``arr2`` and ``a + b == target``. Pairs preserve ``arr1`` iteration order.

Example:
    >>> find_pairs([1, 2, 3], [4, 5, 6], 9)
    [(3, 6)]
"""

# WRITE FIND_PAIRS FUNCTION HERE #
def find_pairs(arr1, arr2, target):
    set2 = set(arr2)
    output_list = []
    for item in arr1:
        complement = target - item
        if complement in set2:
            output_list.append((item, complement))
    return output_list
##################################




if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 4, 6, 8, 10]
    target = 7

    pairs = find_pairs(arr1, arr2, target)
    print(pairs)

    """
        EXPECTED OUTPUT:
        ----------------
        [(5, 2), (3, 4), (1, 6)]

    """
