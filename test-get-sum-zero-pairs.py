def get_sum_zero_pairs(input_list):
    """Given a list of numbers,
    return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
#NOTES
    #add item to list if two values sum to zero
    #add pos and neg value pairs
    #values in a list, inside of a list
    #use set()? yes
    #use dictionary? no

    results_zero_list = []
    list_to_set = set(input_list)

    for num in list_to_set:
        #if number is greater than 0, AND has same neg number
        if num >= 0 and -num in list_to_set:
            #if so, append pair of numbers to results_zero_list (in a list pair)
            results_zero_list.append([-num, num])


    return sorted(results_zero_list)
print get_sum_zero_pairs([1, 2, 3, -2, -1])
print get_sum_zero_pairs([3, -3, 2, 1, -2, -1])
print get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1])
print get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0])




#scratch paper
# sets = set()
#     results_zero_list = set()

#     for number in input_list:
#         if -number in sets:
#             results_zero_list.append(number + -number)




