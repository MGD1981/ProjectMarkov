# coding=utf-8
from sys import exit
from random import randint

CSI="\x1B["
reset=CSI+"m"
# sample: print CSI+"31;40m" + "Colored Text" + CSI + "0m"



class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()



def cls():
    print CSI+"30;47m" + CSI+"2J" # clears screen

def aiturn(aicolor, boarddata):
    # FIRST the computer needs to test if any move will cause it to win.
    # This might be done more efficiently if it revolves around the player's
    # last move.
    
    # If player is one move from a win, no chance for offensive.
    # Need-Block Test:
    
    movetype = randint(1,5)
    if movetype < 4:
        move = aioffense(aicolor, boarddata)
    else:
        move = aidefense(aicolor, boarddata)
    return move
    
    
def aioffense(aicolor, boarddata):
    if aicolor == 'red':
        t = 1
    else:
        t = -1
        
    


def wincheck(redturn, boarddata):
    if redturn:
        t = 1
    else:
        t = -1
    x = 0; y = 0
    # Horizontal test
    while y < 6:
        if boarddata[x][y] != t:
            x += 1
        elif boarddata[x+1][y] != t:
            x += 1
        elif boarddata[x+2][y] != t:
            x += 1
        elif boarddata[x+3][y] != t:
            x += 1
        else:
            if redturn:
                return 'red'
            else:
                return 'green'    
        if x > 3:
            x = 0; y += 1
    x = 0; y = 0
    # Vertical test
    while y < 3:
        if boarddata[x][y] != t:
            x += 1
        elif boarddata[x][y+1] != t:
            x += 1
        elif boarddata[x][y+2] != t:
            x += 1
        elif boarddata[x][y+3] != t:
            x += 1
        else:
            if redturn:
                return 'red'
            else:
                return 'green'    
        if x > 6:
            x = 0; y += 1
    x = 0; y = 0
    # Diagonal-right test
    while y < 3:
        if boarddata[x][y] != t:
            x += 1
        elif boarddata[x+1][y+1] != t:
            x += 1
        elif boarddata[x+2][y+2] != t:
            x += 1
        elif boarddata[x+3][y+3] != t:
            x += 1
        else:
            if redturn:
                return 'red'
            else:
                return 'green'    
        if x > 3:
            x = 0; y += 1
    x = 3; y = 0
    # Diagonal-left test
    while y < 3:
        if boarddata[x][y] != t:
            x += 1
        elif boarddata[x-1][y+1] != t:
            x += 1
        elif boarddata[x-2][y+2] != t:
            x += 1
        elif boarddata[x-3][y+3] != t:
            x += 1
        else:
            if redturn:
                return 'red'
            else:
                return 'green'
        if x > 6:
            x = 3; y += 1
         
    return 'none'

def dispboard(redturn, ai, boarddisp):
    # Display the board
    cls()
    if redturn:
        print CSI+"31m" + "Red" + CSI+"30m" + "'s turn     ┌─┬─┬─┬─┬─┬─┬─┐"
    else:
        print CSI+"32m" + "Green" + CSI+"30m" + "'s turn   ┌─┬─┬─┬─┬─┬─┬─┐"
    y=0
    print"               │%s│%s│%s│%s│%s│%s│%s│" % (
            boarddisp[0][y],boarddisp[1][y],boarddisp[2][y],boarddisp[3][y],
            boarddisp[4][y],boarddisp[5][y],boarddisp[6][y])
    print"               ├─┼─┼─┼─┼─┼─┼─┤"
    y+=1
    print"               │%s│%s│%s│%s│%s│%s│%s│" % (
            boarddisp[0][y],boarddisp[1][y],boarddisp[2][y],boarddisp[3][y],
            boarddisp[4][y],boarddisp[5][y],boarddisp[6][y])
    print"               ├─┼─┼─┼─┼─┼─┼─┤"
    y+=1
    print"               │%s│%s│%s│%s│%s│%s│%s│" % (
            boarddisp[0][y],boarddisp[1][y],boarddisp[2][y],boarddisp[3][y],
            boarddisp[4][y],boarddisp[5][y],boarddisp[6][y])
    print"               ├─┼─┼─┼─┼─┼─┼─┤"
    y+=1
    print"               │%s│%s│%s│%s│%s│%s│%s│" % (
            boarddisp[0][y],boarddisp[1][y],boarddisp[2][y],boarddisp[3][y],
            boarddisp[4][y],boarddisp[5][y],boarddisp[6][y])
    print"               ├─┼─┼─┼─┼─┼─┼─┤"
    y+=1
    print"               │%s│%s│%s│%s│%s│%s│%s│" % (
            boarddisp[0][y],boarddisp[1][y],boarddisp[2][y],boarddisp[3][y],
            boarddisp[4][y],boarddisp[5][y],boarddisp[6][y])
    print"               ├─┼─┼─┼─┼─┼─┼─┤"
    y+=1
    print"               │%s│%s│%s│%s│%s│%s│%s│" % (
            boarddisp[0][y],boarddisp[1][y],boarddisp[2][y],boarddisp[3][y],
            boarddisp[4][y],boarddisp[5][y],boarddisp[6][y])
    print"               └─┴─┴─┴─┴─┴─┴─┘"

    if ai and not redturn:
        print "\nComputer's turn; hit any key.\n"
        getch() #Placeholder; THIS IS WHERE YOU RUN THE AI
    else:
        print ("Select file:    " + CSI+"34;1m" + "1 2 3 4 5 6 7    Q" +
               CSI+"30;21m" + "uit")
        print "\n"
    
def play(redturn, ai, boarddisp, boarddata, turnnum):
    dispboard(redturn, ai, boarddisp)
    if redturn:
        txtcolor = CSI+"31m"
    else:
        txtcolor = CSI+"32m"
    
    # Stalemate test
    turnnum += 1
    if turnnum == (6 * 7) + 1:
        print "Stalemate!\n"
        print CSI+"0m" # resets color
        exit()
            
    choice = 0
    while choice == 0:
        choice = getch()
        if choice == 'q' or choice == 'Q':
            print "\n"
            print CSI+"0m" # resets color
            exit()
        try:
            choice = int(choice)
        except ValueError:
            choice = 0
        if choice < 1 or choice > 7 or boarddata[choice-1][0] != 0:
            choice = 0
    # Red = 1, Green = -1
    if redturn:
        polarity = 1
    else:
        polarity = -1
    y = 5
    while boarddata[choice-1][y] != 0:
        y -= 1
    boarddata[choice-1][y] = polarity
    boarddisp[choice-1][y] = txtcolor + "○" + CSI+"30m"
    # See if that's a win
    whowon = wincheck(redturn, boarddata)
    if whowon == 'none':
        redturn = not redturn
        play(redturn, ai, boarddisp, boarddata, turnnum)
    else:
        if whowon == 'red':
            whowon = CSI+"31m" + "Red" + CSI+"30m"
        else:
            whowon = CSI+"32m" + "Green" + CSI+"30m"
        dispboard(redturn, ai, boarddisp)
        print "%s is the winner!\n" % whowon
        print CSI+"0m" # resets color
        exit() 
        
    

    
def boardsetup():
    # board is 7x6 matrix
    boarddisp = [[" " for x in xrange(6)] for x in xrange(7)]
    boarddata = [[0 for x in xrange(6)] for x in xrange(7)]
    return boarddisp, boarddata
    
def intro():
    cls()
    print "** CONNECT FOUR!! **"
    print "\nWhat type of game would you like to play?"
    print "\n" + CSI+"1m" + "1)" + CSI+"21m" + " One player"
    print CSI+"1m" + "2)" + CSI+"21m" + " Two players"
    print "\n\n\n" + CSI+"1m" + "Q)" + CSI+"21m" + " Quit\n\n\n"
    choice = getch()
    if choice == "Q" or choice == "q":
        print "\nGoodbye!"
        print CSI+"0m" # resets color
        exit()
    elif choice == '1':
        ai = True
    elif choice == '2':
        ai = False
    else:
        intro()
    redturn = True
    turnnum = 0
    boarddisp, boarddata = boardsetup()
    play(redturn, ai, boarddisp, boarddata, turnnum)


cls()
intro()


print CSI+"0m" # resets color
