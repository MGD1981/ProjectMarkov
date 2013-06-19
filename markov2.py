from sys import argv
from random import choice

script, file1 = argv

def genchain(dictsource, length):
    """
    Returns a string 'length' words long, based on dictionary 'dictsource'
    and generated with a Markov chain algorithm."""
    print "\nGenerating Markov chain...\n"
    newtext = []
    word = choice(dictsource.keys())

    while length > 0:
        word = choice(dictsource[word])
        newtext.append(word)
        length -= 1

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
        oldword = word
        word = x
   
    return worddict 



print "\nHow many words would you like to generate?"
try:
    w = int(raw_input(">> "))
except ValueError:
    w = 500
if w <= 0:
    w = 500

worddict = createlib(file1)
newtext = genchain(worddict, w)

print newtext

