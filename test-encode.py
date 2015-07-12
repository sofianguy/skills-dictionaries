def encode(phrase):
    """Given a phrase, replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u". Return the encoded string.

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    # phrase_list = phrase.split()
    new_phrase = ""

    for letter in phrase:
    	if letter == "e":
    		new_phrase = new_phrase + "p"
    	elif letter == "a":
    		new_phrase = new_phrase + "d"
    	elif letter == "t":
    		new_phrase = new_phrase + "o"
    	elif letter == "i":
    		new_phrase = new_phrase + "i"
    	else:
    		new_phrase = new_phrase + letter

    return new_phrase
print encode("You are a beautiful, talented, brilliant, powerful musk ox.")



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