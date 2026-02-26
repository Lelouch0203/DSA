def solveSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []

    # Initialize sets with existing numbers
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                num = board[i][j]
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + j // 3].add(num)
            else:
                empties.append((i, j))

    def backtrack(k=0):
        if k == len(empties):
            return True
        i, j = empties[k]
        b = (i // 3) * 3 + j // 3
        for num in map(str, range(1, 10)):
            if num not in rows[i] and num not in cols[j] and num not in boxes[b]:
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[b].add(num)

                if backtrack(k + 1):
                    return True

                # undo choice
                board[i][j] = "."
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[b].remove(num)
        return False

    backtrack()
board =  [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)
print(board)