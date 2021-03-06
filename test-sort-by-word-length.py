def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

#ULTIMATE GOAL: 
#the_tuple = (length, list_of_words_with_that_length)

    words_dictionary = {}
    for word in words:
    	x = len(word)
    	y = word
    	words_dictionary.setdefault(x, []).append(y)
    words_dictionary = sorted(words_dictionary.items())

    return words_dictionary
print sort_by_word_length(["ok", "an", "apple", "a", "day"])



#SCRATCH PAPER
# sorted_list = []
    # for word in words:
    # 	sorted_list.append(len(word))
    #[2, 2, 5, 1, 3]


# a = sorted_list
    # b = word
    # sorted_list_tuple = (a,b)
    # print sorted_list_tuple


#     sorted_list_tuple = ()
#     sorted_list = []
#     for word in words:
#     	sorted_list = tuple(len(word))
#     	sorted_list_tuple = sorted_list_tuple + sorted_list
#     	print sorted_list
