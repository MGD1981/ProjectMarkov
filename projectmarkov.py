import pdb
import urllib
import htmlslicer
import markov


print "\nPlease enter a URL:"
u = raw_input(">> ")
if len(u) < 1:
    u = 'http://www.thefatalistmarksman.com/'
print "\nHow many words would you like to generate?"
try:
    w = int(raw_input(">> "))
except ValueError:
    w = None
if w <= 0:
    w = None
print "\nPlease be patient as we retrieve web content...\n"
f = urllib.urlopen(u, 'r')
s = f.read()
f.close()

slicedcontent = htmlslicer.slice(s) 

newtext = markov.genchain(slicedcontent, w)

print newtext

