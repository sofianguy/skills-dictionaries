def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed
    without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    removed_list = []
    for word in words:
        if word not in removed_list:
            removed_list.append(word)

    return removed_list

print remove_duplicates(["rose", "is", "a", "rose", "is", "a", "rose"])
print remove_duplicates(["Rose", "is", "a", "rose", "is", "a", "rose"])