board=  [["8","3",".", ".","7",".", ".",".","."]
,        ["6",".",".", "1","9","5", ".",".","."]
        ,[".","9",".",".",".",".",".","6","."]
        ,[".",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
def isValidSudoku(board):
    
    row_maps=[[] for _ in range(9)]
    col_maps=[[] for _ in range(9)]
    box_maps=[[] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            num=board[i][j]
            if num == '.':
                continue
            else:
                if num in row_maps[i] or num in col_maps[j] or num in box_maps[(i//3)*3+((j//3))]:
                    print(f"Failed at {i},{j} repeated {num}")
                    return False 
                else:
                    row_maps[i].append(num)
                    col_maps[j].append(num)
                    box_maps[(i//3)*3+((j//3))].append(num)
    return True
print(isValidSudoku(board))