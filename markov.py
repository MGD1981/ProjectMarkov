from random import randint
<<<<<<< HEAD
import datetime
=======
>>>>>>> 54e6074016e74fb60f042145d9c9f103ce227f21

def genchain(textsource, length=500):
    """Returns a string 'length' words long, based on list 'textsource' and
       generated with a Markov chain algorithm."""
    print "\nGenerating Markov chain...\n"
<<<<<<< HEAD

    t = datetime.datetime.now()

=======
>>>>>>> 54e6074016e74fb60f042145d9c9f103ce227f21
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

<<<<<<< HEAD
    print datetime.datetime.now() - t

=======
>>>>>>> 54e6074016e74fb60f042145d9c9f103ce227f21
    return " ".join(newtext)
