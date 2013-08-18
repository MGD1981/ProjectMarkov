from markov_in_line import genchain
from sys import argv

script, file1 = argv

text = open(file1).read().split(" ")
print genchain(text)
