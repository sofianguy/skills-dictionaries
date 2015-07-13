def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    # list_to_dict = dict(zip(list1, list2))
    dict_for_zeros = {}
    for item1 in list1:     #look at first item in list1
        for item2 in list2:    #look at second item in list2
            if item1 == item2:    #if the two items are the same...
                dict_for_zeros[item1] = item1 #add item1 as key, item1 as value

    return dict_for_zeros.keys()    #return keys from common_dict in a list
print find_unique_common_items([1, 2, 3, 4], [1, 2])
print find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2])


#SOLUTION WITHOUT USING DICTIONARY
#     combined_list = set(list1)&set(list2)

#     return combined_list
# print sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
# print sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))