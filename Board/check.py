def can_be_placed_Horizontal(board,i,j,word):
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

def can_be_placed_Vertical(board, i, j, word):
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