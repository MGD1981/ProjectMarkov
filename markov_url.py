from sys import argv
import urllib
import htmlslicer
import markov_in_line

if len(argv) > 1:
    script, file1 = argv

if len(argv) < 2:
    print "\nPlease enter a URL:"
    u = raw_input(">> ")
    if len(u) < 1:
        u = 'http://www.thefatalistmarksman.com/'
print "\nHow many words would you like to generate?"
try:
    w = int(raw_input(">> "))
except ValueError:
    w = 500
if w <= 0:
    w = 500

if len(argv) < 2: 
    print "\nPlease be patient as we retrieve web content...\n"
    f = urllib.urlopen(u, 'r')
else:
    f = open(file1, 'r')

s = f.read()
f.close()

if len(argv) < 2:
    content = htmlslicer.slice(s) 
else:
    content = s.split()

newtext = markov_in_line.genchain(content, w)

print newtext

