import json
from random import choice
import pdb
import time

def resetboard():
    return [0 for x in range(0,9)]

def evalboard(board):

    if (abs((board[0] + board[1] + board[2])) == 3 or
          abs((board[3] + board[4] + board[5])) == 3 or
          abs((board[6] + board[7] + board[8])) == 3 or
          abs((board[0] + board[4] + board[8])) == 3 or
          abs((board[2] + board[4] + board[6])) == 3 or
          abs((board[0] + board[3] + board[6])) == 3 or
          abs((board[1] + board[4] + board[7])) == 3 or
          abs((board[2] + board[5] + board[8])) == 3):
        return 1
    else:
        return 0

def turn(board):
    if sum(board) == 0:
        return 1
    return -1
 
def minimax(board):

    p = turn(board)
    alpha = -10  
    best_move = -1

    for x in range(0,9):
        if board[x] != 0: continue
        board[x] = p
        if winstate(board) != 0:
            alpha = evalboard(board)
            board[x] = 0
            return (alpha, 0)
        prev_a = alpha
        alpha = max(alpha, -1 * minimax(board)[0])
        if alpha > prev_a:        
            best_move = x
        board[x] = 0
    return (alpha, best_move)


def selectmove(board):
    p = turn(board)    
    if board.count(0) == 1:
        best_move = board.index(0)
    else:
        _, best_move = minimax(board)
    board[best_move] = p
    return board

def winstate(board):
    if 0 not in board: return  2
    if evalboard(board) != 0: return 1
    return 0

def printboard(board):
    print '\n'
    s = "".join((str(board)))
    s = s.replace('-1','O').replace('1','X').replace('0','_').replace(
        ',',"").replace('[',"").replace(']', "")
    print s[0:5]
    print s[6:11]
    print s[12:17]

board = resetboard()

while winstate(board) == 0:
    printboard(board)
    board = selectmove(board)


if winstate(board) == 1:
    print "\nWinner!"
else:
    print "\nStalemate!"
printboard(board)
