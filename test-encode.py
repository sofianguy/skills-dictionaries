def encode(phrase):
    """Given a phrase, replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u". Return the encoded string.

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """
#NOTES:
    #keys are letters being replaced
    #values are letters you want to replace with
	#lookup = {
	#   "e": "p",
	#   "a": "d",
	#   ...
	# }
	
    replacement_dict = {'e': 'p', 'a': 'd', 't': 'o', 'i': 'u'}
    new_phrase = ""

    for letter in phrase:
    	if letter in replacement_dict:
			new_phrase = new_phrase + replacement_dict[letter]
    	else:
			new_phrase = new_phrase + letter

    return new_phrase
print encode("You are a beautiful, talented, brilliant, powerful musk ox.")



#SOLUTION WITHOUT DICTIONARY
#     new_phrase = ""

#     for letter in phrase:
#     	if letter == "e":
#     		new_phrase = new_phrase + "p"
#     	elif letter == "a":
#     		new_phrase = new_phrase + "d"
#     	elif letter == "t":
#     		new_phrase = new_phrase + "o"
#     	elif letter == "i":
#     		new_phrase = new_phrase + "u"
#     	else:
#     		new_phrase = new_phrase + letter

#     return new_phrase
# print encode("You are a beautiful, talented, brilliant, powerful musk ox.")


#SCRATCH PAPER
 # for letter in phrase:
 #    	if letter == "e":
 #    		new_phrase = phrase.replace(letter, "p")
 #    	elif letter == "a":
 #    		new_phrase = phrase.replace(letter,"d")
 #    	elif letter == "t":
 #    		new_phrase = phrase.replace(letter, "o")
 #    	elif letter == "i":
 #    		new_phrase = phrase.replace(letter, "i")
 #    	else:
 #    		new_phrase = letter

 # for letter in phrase:
 #    	if letter == "e":
 #    		new_phrase = new_phrase + "p"
 #    	elif letter == "a":
 #    		new_phrase = new_phrase + "d"
 #    	elif letter == "t":
 #    		new_phrase = new_phrase + "o"
 #    	elif letter == "i":
 #    		new_phrase = new_phrase + "i"
 #    	else:
 #    		new_phrase = letter