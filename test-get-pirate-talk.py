def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    english_words = ['sir', 'hotel', 'student', 'boy', 'madam', 'professor', \
    'restaurant', 'your', 'excuse', 'students', 'are', 'lawyer', 'the', 'restroom', \
    'my', 'hello', 'is', 'man']
    pirate_words = ['matey', 'fleabag inn', 'swabbie', 'matey', 'proud beauty', \
    'foul blaggart', 'galley', 'yer', 'arr', 'swabbies', 'be', 'foul blaggart', "th'", \
    'head', 'me', 'avast', 'be', 'matey']
# phrase = "my stduent is not a man"
    eng_pir_dict = dict(zip(english_words, pirate_words))
    phrase_list = phrase.split()
    #phrase_list = ['my', 'student', 'is', 'not', 'a', 'man!']

    pirate_talk = phrase_list.pop(0)
    if pirate_talk in eng_pir_dict:
        pirate_talk = eng_pir_dict[pirate_talk]

    # pirate_talk = 'my'
    # phrase_list = ['student', 'is', 'not', 'a', 'man!']
    for word in phrase_list:
        #word = 'student'
        if word in eng_pir_dict:
            pirate_talk = pirate_talk +  " " + eng_pir_dict[word]
            # pirate_talk = 'my swabbie'
        else:
            pirate_talk = pirate_talk + " " + word
    # " ".join(word)
#meswabbiebenotaman!

    return pirate_talk
print get_pirate_talk("my student is not a man")
print get_pirate_talk("my student is not a man!")



