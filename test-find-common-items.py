def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.

    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    common_items_list = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common_items_list.append(item1) #add item1 to new list

    return common_items_list
print find_common_items([1, 2, 3, 4], [1, 2])
print find_common_items([1, 2, 3, 4], [1, 1, 2, 2])
print find_common_items([1, 1, 2, 2], [1, 2, 3, 4])