from sys import argv
from random import choice
<<<<<<< HEAD
import datetime
import pdb

if __name__ == '__main__':
    script, file1 = argv
=======

script, file1 = argv
>>>>>>> 54e6074016e74fb60f042145d9c9f103ce227f21

def genchain(dictsource, length):
    """
    Returns a string 'length' words long, based on dictionary 'dictsource'
    and generated with a Markov chain algorithm."""
    print "\nGenerating Markov chain...\n"
<<<<<<< HEAD

    t = datetime.datetime.now()

=======
>>>>>>> 54e6074016e74fb60f042145d9c9f103ce227f21
    newtext = []
    word = choice(dictsource.keys())

    while length > 0:
        word = choice(dictsource[word])
        newtext.append(word)
        length -= 1

<<<<<<< HEAD
    print datetime.datetime.now() - t

=======
>>>>>>> 54e6074016e74fb60f042145d9c9f103ce227f21
    return " ".join(newtext)
    

def createlib(text):
    """
    Takes text file and creates a library, linking each word in the files
    to the word that comes after it, and the number of times that sequence
    occurs."""
    print "\nCreating associative library of words..."
    worddict = {}
    text = open(text).read().split(" ")
    word = choice(text)

    for x in text:
        worddict.setdefault(word, []).append(x)
<<<<<<< HEAD
        word = x
    return worddict 


=======
        oldword = word
        word = x
   
    return worddict 



>>>>>>> 54e6074016e74fb60f042145d9c9f103ce227f21
print "\nHow many words would you like to generate?"
try:
    w = int(raw_input(">> "))
except ValueError:
    w = 500
if w <= 0:
    w = 500

worddict = createlib(file1)
<<<<<<< HEAD

=======
>>>>>>> 54e6074016e74fb60f042145d9c9f103ce227f21
newtext = genchain(worddict, w)

print newtext

