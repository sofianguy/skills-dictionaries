def adv_alpha_sort_by_word_length(words):
    """    
    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

#NOTES:
    #same as problem #7(sort_by_word_length)?
    #'an' and 'ok'.... => 'words should be in alpha order'
    #use .sort() or .sorted() only once
    #sort just the values? keys will stay ordered?


    words_dictionary = {}

    for word in words:
        x = len(word)
        y = word
        words_dictionary.setdefault(x, []).append(y)
    words_dictionary = words_dictionary.items()

    sorted_values_list = []
    for values in words_dictionary.values(): 
        sorted_values_list.append(values.sort()) #sort just values

    return words_dictionary

print adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
# => [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]


#SCRATCH PAPER:

#     words_dictionary = {}
#     for word in words:
#         x = len(word)
#         y = word
#         words_dictionary.setdefault(x, []).append(y)
#     words_dictionary = sorted(words_dictionary.items())

    # return words_dictionary
    # print sort_by_word_length(["ok", "an", "apple", "a", "day"])