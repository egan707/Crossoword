def fill_Vertical(board,i,j,word):
    res=[]
    for k in range(len(word)):
        if board[i+k][j]=='-':
            board[i+k][j]=word[k]
            res.append(True)
        else:
            res.append(False)
    return res

def revert_Vertical(board,i,j,b):
    for k in range(len(b)):
        if b[k]:
            board[i+k][j]='-'
    
def fill_Horizontal(board,i,j,word):
    res=[]
    for k in range(len(word)):
        if board[i][k+j]=='-':
            board[i][k+j]=word[k]
            res.append(True)
        else:
            res.append(False)
            
    return res
    
def revert_Horizontal(board,i,j,b):
    for k in range(len(b)):
        if b[k]:
            board[i][k+j]='-'