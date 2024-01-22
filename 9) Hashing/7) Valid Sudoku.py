# https://www.interviewbit.com/problems/valid-sudoku/
# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First validating row and col
        row = {}
        col = {}
        n = len(board)
        # To generate boxes for every i%no_of_boxes th row
        no_of_boxes = int(n**(1/2))
        
        for i in range(n):
            row = {}
            col = {}
            # Generating the box with empty dict
            if i%no_of_boxes == 0:
                boxes = [{} for x in range(no_of_boxes)]
                
            for j in range(n):
                # Checking for valid row
                if board[i][j] in row:
                    return 0
                if board[i][j] != ".":
                    row[board[i][j]] = 1
                
                # Checking for column
                if board[j][i] in col:
                    return 0
                if board[j][i] != ".":
                    col[board[j][i]] = 1
                
                
                # Checking for current applicable box
                current_box = boxes[j//no_of_boxes]
                if board[i][j] in current_box:
                    return 0
                if board[i][j] != ".":
                    current_box[board[i][j]] = 1
        return 1