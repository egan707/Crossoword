#!/bin/python3

import math
import os
import random
import re
import sys

from Board import action, check, print_board


#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#
"""
def print_board(borad):
    for r in borad:
        print(''.join(r))
    

def can_be_placed_H(board,i,j,word):
    if j-1>0 and board[i][j-1] !='+':
        return False
    if j+len(word)<10 and board[i][j+len(word)]!='+':
        return False
    
    
    for k in range(len(word)):
        if j+k>=len(board):
            return False
        if board[i][j+k] in ['-',word[k]]:
            continue
        else:
            return False    
    return True

def fill_H(board,i,j,word):
    res=[]
    for k in range(len(word)):
        if board[i][k+j]=='-':
            board[i][k+j]=word[k]
            res.append(True)
        else:
            res.append(False)
            
    return res
    
def revert_H(board,i,j,b):
    for k in range(len(b)):
        if b[k]:
            board[i][k+j]='-'
     
    
def can_be_placed_V(board,i,j,word):
    if i-1>0 and board[i-1][j] !='+':
        return False
    if i+len(word)<10 and board[i+len(word)][j]!='+':
        return False
    
    
    for k in range(len(word)):
        if i+k>=len(board):
            return False
        if board[i+k][j] in ['-',word[k]]:
            continue
        else:
            return False    
    return True
    
def fill_Vertical(board,i,j,word):
    res=[]
    for k in range(len(word)):
        if board[i+k][j]=='-':
            board[i+k][j]=word[k]
            res.append(True)
        else:
            res.append(False)
    return res

def revert_V(board,i,j,b):
    for k in range(len(b)):
        if b[k]:
            board[i+k][j]='-'
"""   

def solve(board, words,index):
    
    # Write your code here
    if index==len(words):
        print_board.display(board)
        return board
    word=words[index]
    for i in range(10):
        for j in range(10):
            if board[i][j] in ['-',word[0]]:
                if check.can_be_placed_Horizontal(board,i,j,word):
                    b=[]
                    b=action.fill_Horizontal(board,i,j,word)
                    solve(board,words,index+1)
                    action.revert_Horizontal(board,i,j,b)
                if check.can_be_placed_Vertical(board,i,j,word):
                    b=[]
                    b=action.fill_Vertical(board,i,j,word)
                    solve(board,words,index+1)

                    action.revert_Vertical(board,i,j,b)
    # print_board(board)
    return 
def list_converter(board_row):
    return list(board_row)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    board = []
    # print('the board')
    crossword_item='''+-++++++++
                    +-++++++++
                    +-++++++++
                    +-----++++
                    +-+++-++++
                    +-+++-++++
                    +++++-++++
                    ++------++
                    +++++-++++
                    +++++-++++'''
    # for _ in range(10):
    #     crossword_item = input()
    #     board.append(list(crossword_item))
    # board=list(map(list_converter,crossword_item.split()))
    # board = [list(row) for row in crossword_item.split()]
    board = list(map(list_converter,crossword_item.split()))

    print(board)
    # words = str(input()).split(';')
    words="LONDON;DELHI;ICELAND;ANKARA".strip().split(';')
    print(crossword_item)
    
    
    solve(board, words,0)
        

    # print_board(board)
    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
