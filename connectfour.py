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

def findy(board, x):
    y = 5
    while board[x][y] != 0:
        y -= 1
    return y

def minimax(depth, difftest, boardproxy, aicolor):    
    #pdb.set_trace()
    value = assignvalue(boardproxy, aicolor)
    if depth == 0 or value != 0:
        print value, depth #xxx
        return value

    maxval = [-float('inf'),randint(0,6)]
    for x in range(len(boardproxy)):
        if boardproxy[x][0] != 0:
            continue
        y = findy(boardproxy, x)
        boardproxy[x][y] = aicolor
        value = (-minimax(depth - 1, difftest, boardproxy, -aicolor))
        if maxval[0] < value:
            maxval[1] = x
        maxval = [max(maxval[0], value), maxval[1]]
        boardproxy[x][y] = 0
    if depth == difftest:
        if maxval[0] == 0:
            return 7 # Will turn 7 into randint, or move to another test
                     # depending on difficulty.
        else:
            return maxval[1]
    else:
        print maxval, depth #xxx
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


def dispboard(redturn, ai, boarddisp, aicolor):
    # Display the board
    cls()
    if redturn:
        player = CSI+"31m" + "Red" + CSI+"30m" + "'s turn  "
    else:
        player = CSI+"32m" + "Green" + CSI+"30m" + "'s turn"
    print player + "   ┌─┬─┬─┬─┬─┬─┬─┐"
    for y in range(6):
        print"               │%s│%s│%s│%s│%s│%s│%s│" % (
                boarddisp[0][y],boarddisp[1][y],boarddisp[2][y],
                boarddisp[3][y],boarddisp[4][y],boarddisp[5][y],
                boarddisp[6][y])
        if y != 5:
            print"               ├─┼─┼─┼─┼─┼─┼─┤"
        else:
            print"               └─┴─┴─┴─┴─┴─┴─┘"

    if ai and (
            (not redturn and aicolor == -1) or (redturn and aicolor == 1)):
        print "\nComputer's turn; hit any key.\n"
    else:
        print ("Select column:  " + CSI+"34;1m" + "1 2 3 4 5 6 7    Q" +
               CSI+"30;21m" + "uit")
        print "\n"
    
def play(redturn, ai, boarddisp, boarddata, difficulty, aicolor):
    dispboard(redturn, ai, boarddisp, aicolor)
    if redturn:
        txtcolor = CSI+"31m"
    else:
        txtcolor = CSI+"32m"
    
    # Stalemate test
    toprow = [(boarddata[x][0]) for x in range(len(boarddata))]
    if 0 not in toprow:
        print "Stalemate!\n"
        print CSI+"0m" # resets color
        exit()
            
    choice = 0
    while choice == 0:
        choice = getch()
        if ai and (
                (not redturn and aicolor == -1) or (redturn and aicolor == 1)):
            if difficulty == 1:
                choice = minimax(1, 1, boarddata, -aicolor)
            if difficulty >= 2:
                choice = minimax(2, 2, boarddata, -aicolor)
            if difficulty == 4 and choice == 7:
                choice = minimax(difficulty, difficulty,
                                 boarddata, -aicolor)
            choice = choice + 1                   
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
                
        if choice == 8:
            choice = randint(1,7)
            while boarddata[choice-1][0] != 0:
                choice = randint(1,7)
                
                
    # Red = 1, Green = -1
    if redturn:
        polarity = 1
    else:
        polarity = -1
    y = findy(boarddata, choice-1)
    boarddata[choice-1][y] = polarity
    boarddisp[choice-1][y] = txtcolor + "○" + CSI+"30m"
    # See if that's a win
    whowon = assignvalue(boarddata, aicolor)
    if whowon == 0:
        redturn = not redturn
        play(redturn, ai, boarddisp, boarddata, difficulty, aicolor)
    else:
        if whowon < 0:
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
        print "\nSelect a difficulty:"
        print "\n" + CSI+"1m" + "1)" + CSI+"21m" + " Child"
        print CSI+"1m" + "2)" + CSI+"21m" + " Normal"
        print CSI+"1m" + "3)" + CSI+"21m" + " Difficult"
        print "\n\n\n" + CSI+"1m" + "Q)" + CSI+"21m" + " Quit\n\n\n"
        choice = getch()
        if choice == "Q" or choice == "q":
            print "\nGoodbye!"
            print CSI+"0m" # resets color
            exit()
        elif choice == '1':
            difficulty = 1
        elif choice == '2':
            difficulty = 2
        elif choice == '3':
            difficulty = 4
        else:
            intro()
            
        cls()
        print ("\nWould you like to play as " + CSI+"31m" + "R" +
               CSI+"30m" + "ed or " + CSI+"32m" + "G" + CSI+"30m" + "reen?")
        print "\n(Red player goes first.)"
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
        difficulty = 0
        ai = False
        aicolor = -1
    else:
        intro()
    redturn = True
    boarddisp, boarddata = boardsetup()
    play(redturn, ai, boarddisp, boarddata, difficulty, aicolor)


cls()
intro()


print CSI+"0m" # resets color
