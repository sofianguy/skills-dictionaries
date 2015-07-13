def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """
#NOTES:
    #need a count of how times letter appears
    #put letter as key, count as values
    #
    
    letter_count_dict = {}
    winner_letter = ""
    for letter in input_string:
        



    return winner_letter

print adv_get_top_letter("The rain in spain stays mainly in the plain.")
print adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")