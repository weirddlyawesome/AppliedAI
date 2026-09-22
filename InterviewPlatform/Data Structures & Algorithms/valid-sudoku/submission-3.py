class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                set_= set()
                for row_ in range(row, row+3):
                    for col_ in range(col, col+3):
                        char = board[row_][col_]
                        if char.isalnum() and int(char) in set_:
                            return False
                        elif char.isalnum():
                            set_.add(int(char))

        row, col = 9, 9
       
        for i in range(row):
            set_ = set()
            for j in range(col):
                if board[i][j].isalnum() and int (board[i][j]) in set_:
                    return False
                elif board[i][j].isalnum():
                    set_.add(int(board[i][j]))

        
        for j in range(col):
            set_ = set()
            for i in range(row):
                if board[i][j].isalnum() and int(board[i][j]) in set_:
                    return False
                elif board[i][j].isalnum():
                    set_.add(int(board[i][j]))


        
        return True
