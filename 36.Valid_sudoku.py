from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_length = len(board)
        row_check = set()
        column_check = set()
        # checking each rows and columns for violation of the soduko rules
        for i in range(board_length):
            row_check.clear()
            column_check.clear()
            for j in range(board_length):
                if board[i][j] != ".":
                    if board[i][j] in row_check:
                        return False
                    else:
                        row_check.add(board[i][j])
                    
                if board[j][i] != ".":
                    if board[j][i] in column_check:
                        return False
                    else:
                        column_check.add(board[j][i])                   
                
                
        
        
        
        # for checking each grid for violation of the soduko rules
        grid_1 = set()
        grid_2 = set()
        grid_3 = set()
        for i in range(board_length):
            
            for j in range(board_length):
                grid_count = int(j/3)
                print(board[i][j])
                if board[i][j] == ".":
                    continue
                
                if grid_count == 0:
                    if board[i][j] in grid_1:
                        return False
                    else:
                        grid_1.add(board[i][j])
                elif grid_count == 1:
                    if board[i][j] in grid_2:
                        return False
                    else:
                        grid_2.add(board[i][j])
                elif grid_count == 2:
                    if board[i][j] in grid_3:
                        return False
                    else:
                        grid_3.add(board[i][j])

            if (i+1) % 3 == 0:
                grid_1.clear()
                grid_2.clear()
                grid_3.clear()
                print("cleared")
        
        return True

if __name__ == "__main__":
    output = Solution().isValidSudoku(board=[[".",".","4",".",".",".","6","3","."],
                                             [".",".",".",".",".",".",".",".","."],
                                             ["5",".",".",".",".",".",".","9","."],
                                             [".",".",".","5","6",".",".",".","."],
                                             ["4",".","3",".",".",".",".",".","1"],
                                             [".",".",".","7",".",".",".",".","."],
                                             [".",".",".","5",".",".",".",".","."],
                                             [".",".",".",".",".",".",".",".","."],
                                             [".",".",".",".",".",".",".",".","."]])
    print(output)