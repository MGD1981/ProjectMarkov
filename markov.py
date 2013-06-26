from random import randint
import datetime

def genchain(textsource, length=500):
    """Returns a string 'length' words long, based on list 'textsource' and
       generated with a Markov chain algorithm."""
    print "\nGenerating Markov chain...\n"

    t = datetime.datetime.now()

    chainlen = len(textsource) - 1
    loc = randint(0, chainlen)
    newtext = []
    
    while length > 0:
        current_word = textsource[loc]
        newtext.append(current_word)
        occurences = textsource.count(textsource[loc])
        r = randint(1, occurences)
        c = 0
        loc = 0
        while c < r:
            if textsource[loc] == current_word:
                c += 1
            loc += 1
            if loc > chainlen:
                loc = randint(0, chainlen)
        length -= 1

    print datetime.datetime.now() - t

    return " ".join(newtext)
