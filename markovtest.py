from random import randint
import time
import os

def markov(pos):
    y = randint(1,2)
    if y == 1:
        pol = 1
    else:
        pol = -1
    y = randint(1, 39)
    if y <= abs(pos):
        if pos > 0:
            pol = -1
        else:
            pol = 1
    return pos + pol

pos = 0
while True:
    print " " * 40,
    if pos > 0:
        print " " * pos,
    else:
        print '\b' * abs(pos),
    print '@'
    time.sleep(.1)
 
    pos = markov(pos)

