# coding=utf-8
import pdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
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


def listcopy2d(li):
    newli = []
    for subli in li:
        newli.append([x for x in subli])
    return newli
    
def findy(board, x):
    y = 5
    while board[x][y] != 0:
        y -= 1
    return y

def minimax(depth, difficulty, boardproxy, aicolor):    
    #pdb.set_trace()
    #value = 0
    if depth == 0:
        value = assignvalue(boardproxy, aicolor)
        return value

    maxval = [-float('inf'),randint(0,6)]
    for x in range(len(boardproxy)):
        if boardproxy[x][0] != 0:
            continue
        #boardproxy = listcopy2d(boarddata)
        y = findy(boardproxy, x)
        boardproxy[x][y] = aicolor
        value = (-minimax(depth - 1, difficulty, boardproxy, -aicolor))
        if maxval[0] < value:
            maxval[1] = x
        maxval = [max(maxval[0], value), maxval[1]]
        boardproxy[x][y] = 0
    if depth == difficulty:
        if maxval[0] == 0:
            return randint(0,6)
        else:
            return maxval[1]
    else:
        return maxval[0]



def assignvalue(boardproxy, aicolor):
    assignedval = 0
    xp = 0; yp = 0
    # Horizontal score
    while yp < 6:
        t = boardproxy[xp][yp]
        if boardproxy[xp][yp] == 0:
            xp += 1
        elif boardproxy[xp+1][yp] != t:
            xp += 1
        elif boardproxy[xp+2][yp] != t:
            xp += 1
        elif boardproxy[xp+3][yp] != t:
            xp += 1
        else:
            assignedval += float('inf') * t * aicolor
            xp += 1   
        if xp > 3:
            xp = 0; yp += 1
    xp = 0; yp = 0
    # Vertical score
    while yp < 3:
        t = boardproxy[xp][yp]
        if boardproxy[xp][yp] == 0:
            xp += 1
        elif boardproxy[xp][yp+1] != t:
            xp += 1
        elif boardproxy[xp][yp+2] != t:
            xp += 1
        elif boardproxy[xp][yp+3] != t:
            xp += 1
        else:
            assignedval += float('inf') * t * aicolor
            xp += 1
        if xp > 6:
            xp = 0; yp += 1
    xp = 0; yp = 0
    # Diagonal-right score
    while yp < 3:
        t = boardproxy[xp][yp]
        if boardproxy[xp][yp] == 0:
            xp += 1
        elif boardproxy[xp+1][yp+1] != t:
            xp += 1
        elif boardproxy[xp+2][yp+2] != t:
            xp += 1
        elif boardproxy[xp+3][yp+3] != t:
            xp += 1
        else:
            assignedval += float('inf') * t * aicolor
            xp += 1
        if xp > 3:
            xp = 0; yp += 1
    xp = 3; yp = 0
    # Diagonal-left score
    while yp < 3:
        t = boardproxy[xp][yp]
        if boardproxy[xp][yp] == 0:
            xp += 1
        elif boardproxy[xp-1][yp+1] != t:
            xp += 1
        elif boardproxy[xp-2][yp+2] != t:
            xp += 1
        elif boardproxy[xp-3][yp+3] != t:
            xp += 1
        else:
            assignedval += float('inf') * t * aicolor
            xp += 1
        if xp > 6:
            xp = 3; yp += 1
    return assignedval




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
                return 1
            else:
                return -1    
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
                return 1
            else:
                return -1    
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
                return 1
            else:
                return -1    
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
                return 1
            else:
                return -1
        if x > 6:
            x = 3; y += 1
         
    return 'none'

def dispboard(redturn, ai, boarddisp, aicolor):
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

    if ai and (
            (not redturn and aicolor == -1) or (redturn and aicolor == 1)):
        print "\nComputer's turn; hit any key.\n"
        #getch()
    else:
        print ("Select file:    " + CSI+"34;1m" + "1 2 3 4 5 6 7    Q" +
               CSI+"30;21m" + "uit")
        print "\n"
    
def play(redturn, ai, boarddisp, boarddata, turnnum, difficulty, aicolor):
    dispboard(redturn, ai, boarddisp, aicolor)
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
        if ai and (
                (not redturn and aicolor == -1) or (redturn and aicolor == 1)):
            choice = (minimax(difficulty, difficulty, 
                              listcopy2d(boarddata), -aicolor) + 1)
        else:     
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
    #pdb.set_trace()
    while boarddata[choice-1][y] != 0:
        y -= 1
    boarddata[choice-1][y] = polarity
    boarddisp[choice-1][y] = txtcolor + "○" + CSI+"30m"
    # See if that's a win
    whowon = wincheck(redturn, boarddata)
    if whowon == 'none':
        redturn = not redturn
        play(redturn, ai, boarddisp, boarddata, turnnum, difficulty, aicolor)
    else:
        if whowon == 1:
            whowon = CSI+"31m" + "Red" + CSI+"30m"
        else:
            whowon = CSI+"32m" + "Green" + CSI+"30m"
        dispboard(redturn, ai, boarddisp, aicolor)
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
    aicolor = 0
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
        cls()
        print ("\nWould you like to play as " + CSI+"31m" + "R" +
               CSI+"30m" + "ed or " + CSI+"32m" + "G" + CSI+"30m" + "reen?")
        print "\n\n\n" + CSI+"1m" + "Q)" + CSI+"21m" + " Quit\n\n\n"
        choice = getch()
        if choice == "Q" or choice == "q":
            print "\nGoodbye!"
            print CSI+"0m" # resets color
            exit()
        elif choice == 'g' or choice == 'G':
            aicolor = 1
        elif choice == 'r' or choice == 'R':
            aicolor = -1
        else:
            intro()
    elif choice == '2':
        ai = False
    else:
        intro()
    redturn = True
    turnnum = 0
    boarddisp, boarddata = boardsetup()
    difficulty = 2
    play(redturn, ai, boarddisp, boarddata, turnnum, difficulty, aicolor)


cls()
intro()


print CSI+"0m" # resets color
